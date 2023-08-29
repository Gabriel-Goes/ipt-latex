# -*- coding: utf-8 -*-
import csv

# Nome do arquivo de entrada CSV
input_csv = "../csv/events-2023-06-01-IT.csv"

# Nome do arquivo de saída LaTeX
output_tex = "/home/ipt/documents/ggrl/tarefa_latex/boletim/machadinho/tex/Tabela.tex"

# Abre o arquivo CSV para leitura
with open(input_csv, "r") as csv_file:
    # Lê o conteúdo do CSV
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

# Abre o arquivo LaTeX para escrita
with open(output_tex, "w") as tex_file:
    tex_file.write("\\begin{table}[htb!]\n")
    tex_file.write("    \\begin{center} \n")
    tex_file.write("        \\caption{Dados de Terremotos}\n")
    tex_file.write("        \\renewcommand{\\arraystretch}{1.5} \n")
    tex_file.write("        \\tiny\n")
    tex_file.write("        \\begin{tabular}{ccccS[table-format=6.0]S[table-format=7.0]S[table-format=1.1]cc} \n")
    tex_file.write("            \\toprule\n")

    # Escreve o cabeçalho da tabela
    modified_header = ["{" + col + "}" for col in data[0]]
    tex_file.write("            " + " & ".join(modified_header) + " \\\\\n")
    tex_file.write("            \\midrule\n")

    # Escreve o subcabeçalho da tabela
    modified_subheader = []
    for col in data[1]:
        if "°" in col:
            modified_subheader.append(col.replace("°", "\\textdegree\\hspace{0.25em}"))
        else:
            modified_subheader.append("{" + col + "}")
    tex_file.write("            " + " & ".join(modified_subheader) + " \\\\\n")
    tex_file.write("            \\midrule\n")

    # Escreve os dados da tabela
    for row in data[2:]:
        formatted_row = []
        for col_idx, col in enumerate(row):
            if col_idx == 0:  # First column with underscores
                col_with_backslash = col.replace("_", r"\_")
                formatted_row.append(col_with_backslash)
            elif col_idx == 4 or col_idx == 5:  # Colunas UTM X e UTM Y
                formatted_row.append(str(int(float(col))))
            elif col_idx == 7:
                formatted_row.append("\\num[round-precision=3,round-mode=figures,scientific-notation=true]{" + col + "}")
            else:
                formatted_row.append(col)
        tex_file.write("            " + " & ".join(formatted_row) + " \\\\\n")

    tex_file.write("            \\bottomrule\n")
    tex_file.write("        \\end{tabular}\n")
    tex_file.write("        \\label{tab:dados_terremoto}\n")
    tex_file.write("        \\caption*{Fonte:IPT.}\n")
    tex_file.write("    \\end{center}\n")
    tex_file.write("\\end{table}\n")
