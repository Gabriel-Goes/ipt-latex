# -*- coding: utf-8 -*-
import csv

# Nome do arquivo de entrada CSV
input_csv = "../csv/events.csv"

# Nome do arquivo de saída LaTeX
output_tex = "../tex/tabela_machadinho_boletim.tex"

# Abre o arquivo CSV para leitura
with open(input_csv, "r") as csv_file:
    # Lê o conteúdo do CSV
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

# Abre o arquivo LaTeX para escrita
with open(output_tex, "w") as tex_file:
    tex_file.write("\\section{TABELA DE EVENTOS}\n")
    tex_file.write("\\begin{center}\n")
    tex_file.write("\\scriptsize\n")
    tex_file.write("\\setlength{\\arrayrulewidth}{0.05pt}\n")
    tex_file.write("\\begin{longtable}\
{ccccS[table-format=6.0]S[table-format=7.0]ccc}\n")
    tex_file.write("\\captionsetup{justification=justified,\
singlelinecheck=false}\n")
    tex_file.write("\\caption{Listagem de eventos detectados e categorizados durante o período de interesse.\\\\ A coluna \\textit{Cat} representaria a categoria na qual o evento foi classificado sendo \\textit{Q} = Detonação/Desmontes, \\textit{E} = Sismo Regional e \\textit{I} = Sismo induzido e \\textit{N} = Não-localizável. O valor da energia para os sismos foi obtido a partir da magnitude através da relação proposta por Richter (1958). Fonte: IPT.}\\\\\n")
    tex_file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    tex_file.write("\\hline \\\\[-4ex]\n")
    tex_file.write("\\hline \\\\[-5ex]\n")

    # Escreve o cabeçalho da tabela
    modified_header = ["{" + col + "}" for col in data[0]]
    count = 0
    for id in modified_header:
        count += 1
        if count < len(modified_header):
            tex_file.write("\\multicolumn{1}{c}" + id + " &\n")
        else:
            tex_file.write("\\multicolumn{1}{c}" + id + " \\\\\n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[-5.0ex] \\hline\n")
    tex_file.write("\\\\[-5.0ex]")
    tex_file.write("\n")
    tex_file.write("\n")

    # Escreve o subcabeçalho da tabela
    modified_subheader = []
    for col in data[1]:
        if "°" in col:
            modified_subheader.append(
                col.replace("°", "\\textdegree\\hspace{0.25em}"))
        else:
            modified_subheader.append("{" + col + "}")
    count = 0
    for id in modified_subheader:
        count += 1
        if count < len(modified_subheader):
            tex_file.write("\\multicolumn{1}{c}{\\textit{" + id + "}} & \n")
        else:
            tex_file.write("\\multicolumn{1}{c}{\\textit{" + id + "}} \\\\ \n")

    tex_file.write("\n")
    tex_file.write("\\\\[-5.0ex] \\hline\n")
    tex_file.write("\\\\[-4.0ex]")
    tex_file.write("\n")

    tex_file.write("\\endfirsthead\n")
    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

    tex_file.write("\\hline \\\\[-4ex]\n")
    tex_file.write("\\hline \\\\[-5ex]\n")

    # Escreve o cabeçalho da tabela
    modified_header = ["{" + col + "}" for col in data[0]]
    count = 0
    for id in modified_header:
        count += 1
        if count < len(modified_header):
            tex_file.write("\\multicolumn{1}{c}" + id + " &\n")
        else:
            tex_file.write("\\multicolumn{1}{c}" + id + " \\\\\n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[-5.0ex] \\hline\n")
    tex_file.write("\\\\[-5.0ex]")
    tex_file.write("\n")
    tex_file.write("\n")

    # Escreve o subcabeçalho da tabela
    modified_subheader = []
    for col in data[1]:
        if "°" in col:
            modified_subheader.append(
                col.replace("°", "\\textdegree\\hspace{0.25em}"))
        else:
            modified_subheader.append("{" + col + "}")
    count = 0
    for id in modified_subheader:
        count += 1
        if count < len(modified_subheader):
            tex_file.write("\\multicolumn{1}{c}{\\textit{" + id + "}} & \n")
        else:
            tex_file.write("\\multicolumn{1}{c}{\\textit{" + id + "}} \\\\\n")

    tex_file.write("\n")
    tex_file.write("\\\\[-5.0ex] \\hline\n")
    tex_file.write("\\\\[-4.0ex]")
    tex_file.write("\n")
    tex_file.write("\\endhead\n")
    tex_file.write("\\hline\n")
    tex_file.write("\\caption*{Fonte: IPT.}\n")

    tex_file.write("\n")
    tex_file.write("\\endlastfoot\n")
    tex_file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

    # Escreve os dados da tabela
    for row in data[2:]:
        formatted_row = []
        for col_idx, col in enumerate(row):
            if col_idx == 0:  # First column with underscores
                col_with_backslash = col.replace("_", r"\_")
                formatted_row.append(col_with_backslash)
            elif col_idx == 2:  # Seventh column with comma instead of .
                col_with_backslash = col.replace(".", r",")
                formatted_row.append(col_with_backslash)
            elif col_idx == 3:  # Seventh column with comma instead of .
                col_with_backslash = col.replace(".", r",")
                formatted_row.append(col_with_backslash)
            elif col_idx == 4 or col_idx == 5:  # Colunas UTM X e UTM Y
                formatted_row.append(str(int(float(col))))
            elif col_idx == 6:  # Seventh column with comma instead of .
                col_with_backslash = col.replace(".", r",")
                formatted_row.append(col_with_backslash)
            elif col_idx == 7:
                formatted_row.append("\\num[round-precision=3,\
round-mode=figures,scientific\
-notation=true]{" + col + "}")
            else:
                formatted_row.append(col)
        tex_file.write(" & ".join(formatted_row) + " \\\\\n")

    tex_file.write("\\end{longtable}\n")
    tex_file.write("\\end{center}\n")

print(f" -> Tabela '{output_tex}' gerada com sucesso!")
