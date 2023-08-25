# -*- coding: utf-8 -*-
import csv

# Nome do arquivo de entrada CSV
input_csv = "../csv/events-2023-06-01-IT.csv"

# Nome do arquivo de saída LaTeX
output_tex = "Tabela.tex"

# Abre o arquivo CSV para leitura
with open(input_csv, "r") as csv_file:
    # Lê o conteúdo do CSV
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

# Abre o arquivo LaTeX para escrita
with open(output_tex, "w") as tex_file:
    tex_file.write("\\begin{center}\n")
    tex_file.write("\\begin{table}[htbp]\n")
    tex_file.write("    \\caption{Dados de Terremotos}\n")
    tex_file.write("    \\label{tab:dados_terremoto}\n")
    tex_file.write("    \\renewcommand{\\arraystretch}{1.5} % Ajusta espaçamento entre linhas da tabela\n")
    tex_file.write("    \\small\n")
    tex_file.write("    \\begin{tabular}{ccccccccc} % Defina o número de colunas de acordo com seu arquivo CSV\n")
    tex_file.write("        \\toprule\n")

    # Escreve o cabeçalho da tabela
    tex_file.write("        " + " & ".join(data[0]) + " \\\\\n")
    tex_file.write("        \\midrule\n")

    # Escreve o subcabeçalho da tabela
    tex_file.write("        " + " & ".join(data[1]) + " \\\\\n")
    tex_file.write("        \\midrule\n")

    # Escreve os dados da tabela
    for row in data[2:]:
        formatted_row = []
        for col_idx, col in enumerate(row):
            if col_idx == 4 or col_idx == 5:  # Colunas UTM X e UTM Y
                formatted_row.append(str(int(float(col))))
            else:
                formatted_row.append(col)
        tex_file.write("        " + " & ".join(formatted_row) + " \\\\\n")

    tex_file.write("        \\bottomrule\n")
    tex_file.write("    \\end{tabular}\n")
    tex_file.write("    \\caption*{Fonte:IPT.}")
    tex_file.write("\\end{table}\n")
    tex_file.write("\\end{center}\n")
    tex_file.write("\\newpage\n")

