import pandas as pd
import pygmt
import geopandas as gpd
import os
import tempfile


def plot_evs(fig, data, colour):
    try:
        fig.plot(x=data['lon'], y=data['lat'], fill=colour,
                 pen='white', style='c', size=0.10 * 2 ** data['mag'])
    except Exception as e:
        print(f"Error while plotting events: {e}")


if __name__ == "__main__":
    # Read the events data from the CSV file
    df_events = pd.read_csv('events_processed.csv')

    # Read other geographical data
    gdf = gpd.read_file("/home/ipt/projetos/map_dir/pygmt/ita/ita.gpkg")
    cities = gpd.read_file("/home/ipt/projetos/map_dir/pygmt/ita/cidades_ita.gpkg")
    state_bounds = gpd.read_file("/home/ipt/projetos/map_dir/pygmt/ita/estados_BR.gpkg")

    # Define font and load earth relief data for the map
    font = "12p,Helvetica-Bold,black"
    grid = pygmt.datasets.load_earth_relief(resolution='03s', region='-52.47/-51.74/-27.57/-27.11')

    # Create figure and set configurations
    fig = pygmt.Figure()

    pygmt.config(MAP_FRAME_TYPE='fancy')
    pygmt.config(FORMAT_GEO_MAP="ddd.xx")
    pygmt.config(FONT_ANNOT_PRIMARY='12p,Helvetica')

    # Create the base map with earth-relief and annotations
    pygmt.grd2cpt(grid=grid, cmap='grayC', continuous=False, truncate=[0.15,0.25])
    fig.grdimage(grid=grid, projection="M28c", frame=["a", "WSNE"])
    fig.basemap(frame=["+tMapa de Eventos Sísmicos - Rede ITÁ"])

    # Plot non-event map elements (political divisions, cities, reservoirs)
    fig.plot(data=state_bounds, pen='0.75p,black')
    fig.plot(data=gdf, fill='dodgerblue')
    fig.plot(data=cities, style='d0.3c', fill='black', pen='0.5p,white')

    # Plot the events using the data from the DataFrame
    df_natural = df_events[df_events['label_cat'] == 0]
    df_antrop = df_events[df_events['label_cat'] == 1]

    antrop_falso = df_antrop[df_antrop['pred'] == 0]
    antrop_verdadeiro = df_antrop[df_antrop['pred'] == 1]
    natural_falso = df_natural[df_natural['pred'] == 1]
    natural_verdadeiro = df_natural[df_natural['pred'] == 0]

    plot_evs(fig, natural_falso, 'red')
    plot_evs(fig, natural_verdadeiro, 'blue')

    # Adicionar legendas usando um arquivo temporário
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_legend_file:
        legend_spec = """\
G -0.1c
H 12p,Helvetica Eventos Sísmicos
D 0.2c 1p
N 2
V 0.1c/0.1c/0.1c/0.2c
S 0.3c c 0.1 black 0.1p 0.5c Magnitude Menor
S 0.3c c 0.2 red 0.1p 0.5c Naturais Falsos
G 0.2c
S 0.3c c 0.2 black 0.1p 0.5c Magnitude Média
S 0.3c c 0.2 blue 0.1p 0.5c Naturais Verdadeiros
S 0.3c c 0.3 black 0.1p 0.5c Magnitude Maior
"""
        temp_legend_file.write(legend_spec)
        temp_legend_file_name = temp_legend_file.name

    # Especificação da largura da caixa da legenda
    legend_width = "10c"  # Ajuste a largura conforme necessário
    position = "JBC+o10c/1c+w"+legend_width
    fig.legend(position=position, spec=temp_legend_file_name, box="+gwhite+p1p")

    # Save and display the figure
    fig.savefig('natural_seismic_events_map.png', dpi=300)
    fig.show()
    # Remover o arquivo temporário após o uso
    os.remove(temp_legend_file_name)
