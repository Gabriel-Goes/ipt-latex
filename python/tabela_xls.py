import csv
import xlwt

# Nome do arquivo de entrada CSV
input_csv = "/home/ipt/projetos/ipt-latex/tex/salto_pilao/csv/events-2023-06-01-IT.csv"

# Nome do arquivo de saída Excel
output_xls = "/home/ipt/projetos/ipt-latex/tex/salto_pilao/csv/events-2023-06-01-IT.xls"

# Criando estilos de célula no Excel
header_style = xlwt.easyxf('font: bold 1; align: horiz center;')
subheader_style = xlwt.easyxf('font: italic 1, height 220; align: horiz center;')
data_style = xlwt.easyxf('align: horiz left;')
data_style_numeric = xlwt.easyxf(num_format_str='0')
data_style_scientific = xlwt.easyxf(num_format_str='0.00E+00')

# Cria o workbook e uma sheet
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Eventos')

# Abre o arquivo CSV para leitura
with open(input_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    headers = next(csv_reader)
    subheaders = next(csv_reader)

    # Escreve os cabeçalhos e subcabeçalhos com formatação
    for col_idx, header in enumerate(headers):
        sheet.write(0, col_idx, header, header_style)
    for col_idx, subheader in enumerate(subheaders):
        if "°" in subheader:
            subheader = subheader.replace("°", " degrees")
        sheet.write(1, col_idx, subheader, subheader_style)

    # Escreve os dados com formatação específica para cada coluna
    for row_index, row in enumerate(csv_reader, start=2):
        print(row)
        for col_index, cell in enumerate(row):
            if col_index in {0, 1, 8}:  # Colunas de texto ou com substituições específicas
                sheet.write(row_index, col_index, cell, data_style)
            elif col_index in {2, 3, 4, 5}:  # Colunas numéricas
                cell = int(float(cell))
                sheet.write(row_index, col_index, cell, data_style_numeric)
            elif col_index == 7:  # Notação científica
                sheet.write(row_index, col_index, float(cell), data_style_scientific)
            else:  # Restante dos dados
                sheet.write(row_index, col_index, cell, data_style)

# Salva o workbook no arquivo de saída
workbook.save(output_xls)

print(f" -> Tabela Excel '{output_xls}' gerada com sucesso!")
