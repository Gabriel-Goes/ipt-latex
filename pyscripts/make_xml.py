from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import xml.etree.ElementTree as ET
import os
from tqdm import tqdm
import pandas as pd

# Crie um cliente FDSN
client = Client(base_url='http://localhost:8091')

# Busque eventos em um intervalo de tempo específico
start_time = UTCDateTime("2010-01-01")
end_time = UTCDateTime("2023-12-31")
# Nome da pasta mseed
folder_name = "mseed"
catalog = client.get_events(starttime=start_time,
                            endtime=end_time,
                            includearrivals=True)

# Inicialize um DataFrame para armazenar os dados dos eventos
df_events = pd.DataFrame(columns=['time', 'label_cat', 'mag', 'lat', 'lon'])

# Elemento raiz
root = ET.Element("Seiscomp3")

def create_event_dirname(origin_time):
    return origin_time.strftime("%Y%m%dT%H%M%S")


# Função para determinar a categoria do evento
def get_event_category(event_type):
    category_map = {'earthquake': 0,
                    'quarry blast': 1,
                    'induced or triggered event': 0}
    return category_map.get(event_type, f'X - {event_type}')  # 'X - Tipo do evento' como valor padrão


# Loop através do catálogo e crie a estrutura XML
for event in tqdm(catalog):
    event_el = ET.SubElement(root, "Event")
    ET.SubElement(event_el, "EventID").text = str(event.resource_id)
    if event.preferred_origin() and event.preferred_magnitude():
        preferred_origin_id = str(event.preferred_origin_id)
        ET.SubElement(event_el, "PreferredOriginID").text = preferred_origin_id
        ET.SubElement(event_el, "Event_Class").text = str(event.event_type)
        ET.SubElement(event_el, "Location").text = str(
            event.preferred_origin().latitude) + "," + str(
            event.preferred_origin().longitude) + "," + str(
                event.preferred_origin().depth)
        ET.SubElement(event_el, "Magnitude").text = str(event.preferred_magnitude().mag)
        # Obtenha a origem preferida do evento
        preferred_origin = event.preferred_origin()

        # Adicionando informações ao DataFrame
        event_time = event.preferred_origin().time.strftime("%Y%m%d%H%M%S")
        event_category = get_event_category(event.event_type)
        event_mag = event.preferred_magnitude().mag
        print(event)
        df_events = df_events._append({'time': event_time,
                                       'label_cat': event_category,
                                       'mag': event_mag,
                                       'lat': float(event.preferred_origin().latitude),
                                       'lon': float(event.preferred_origin().longitude)}, ignore_index=True)


        # Loop através de cada arrival na origem preferida
        for arrival in preferred_origin.arrivals:
            arrival_el = ET.SubElement(event_el, "Arrival")
            pick_id = arrival.pick_id
            if pick_id:
                # Tente obter os detalhes do Pick
                try:
                    pick = [p for p in event.picks if p.resource_id == pick_id][0]
                    network_id = pick.waveform_id.network_code
                    station_id = pick.waveform_id.station_code

                    # Adicione as informações ao XML
                    ET.SubElement(arrival_el, "PickID").text = str(pick_id)
                    ET.SubElement(arrival_el, "NetworkID").text = network_id
                    ET.SubElement(arrival_el, "StationID").text = station_id
                    ET.SubElement(arrival_el, "Distance").text = str(arrival.distance)
                    ET.SubElement(arrival_el, "Azimuth").text = str(arrival.azimuth)

                    start_time = pick.time - 30
                    end_time = pick.time + 30
                    origin_time = preferred_origin.time
                    arrival_distance = str(arrival.distance)
                    # df_events = df_events._append({'time': event_time, 'label_cat': event_category, 'distance': arrival_distance}, ignore_index=True)


                except IndexError:
                    print(f" ERROR ---> PickID {pick_id} não encontrado no evento.")

                try:
                    # Obtenha a forma de onda para o evento
                    # write an if statement to check if the network_id is different of IT or MC
                    if network_id == "IT" or network_id == "MC":
                        st = client.get_waveforms(network_id, station_id, "*", "*",start_time,end_time)
                        event_dir = os.path.join(folder_name,create_event_dirname(origin_time))
                        mseed_filename = os.path.join(event_dir,f"{network_id}_{station_id}_{create_event_dirname(origin_time)}.mseed")
                        os.makedirs(event_dir, exist_ok=True)
                        st.write(mseed_filename, format="MSEED")

                    else:
                        print(f' --> ERROR: network_id == {network_id}')
                        pass
                except IndexError:
                    print(f" --> ERROR: PickID {pick_id} não encontrado no evento.")


# Salve o DataFrame em um arquivo CSV
df_events.to_csv('events_processed.csv', index=False)

# Escreva no arquivo XML
tree = ET.ElementTree(root)
tree.write("seiscomp3_events.xml")
