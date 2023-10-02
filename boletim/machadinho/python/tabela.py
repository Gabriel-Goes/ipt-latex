# -*- coding: utf-8 -*-
import csv

# Nome do arquivo de entrada CSV
input_csv = "../csv/events-2023-06-01-IT.csv"

# Nome do arquivo de saída LaTeX
output_tex = "../tex/B_Ma_Tabela.tex"

# Abre o arquivo CSV para leitura
with open(input_csv, "r") as csv_file:
    # Lê o conteúdo do CSV
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)

# Abre o arquivo LaTeX para escrita
with open(output_tex, "w") as tex_file:
    tex_file.write("\\begin{center}\n")
    tex_file.write("\\setcaptionmargin{1cm}\n")
    tex_file.write("\\scriptsize\n")
    tex_file.write("\\begin{longtable}{lcccccccc}\n")
    tex_file.write("\\caption[Exemplo de tabela.]{Dados de Terremotos}\\\\\n")
    tex_file.write("\\hline \\hline\\\\[-2ex]\n")

    # Escreve o cabeçalho da tabela
    modified_header = ["{" + col + "}" for col in data[0]]
    for id in modified_header:
        tex_file.write("\\multicolumn{1}{c}" + id + " &\n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[0.5ex] \\hline\n")
    tex_file.write("\\\\[-1.8ex]")
    tex_file.write("\n")
    tex_file.write("\n")

    # Escreve o subcabeçalho da tabela
    modified_subheader = []
    for col in data[1]:
        if "°" in col:
            modified_subheader.append(col.replace("°", "\\textdegree\\hspace{0.25em}"))
        else:
            modified_subheader.append("{" + col + "}")
    for id in modified_subheader:
        tex_file.write("\\multicolumn{1}{c}" + id + " & \n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[0.5ex] \\hline\n")
    tex_file.write("\\\\[-1.8ex]")
    tex_file.write("\n")
    tex_file.write("\n")

    tex_file.write("\\endfirsthead\n")
    tex_file.write("\n")

    tex_file.write("\\multicolumn{9}{c}{\\footnotesize{{\\slshape{{\\tablename} \\table{}}} - Continuação}}\\\\[0.5ex]\n")
    tex_file.write("\n")

    tex_file.write("\\hline \\hline\\\\[-2ex]\n")
    tex_file.write("\n")

    # Escreve o cabeçalho da tabela
    modified_header = ["{" + col + "}" for col in data[0]]
    for id in modified_header:
        tex_file.write("\\multicolumn{1}{c}" + id + " &\n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[0.5ex] \\hline\n")
    tex_file.write("\\\\[-1.8ex]")
    tex_file.write("\n")
    tex_file.write("\n")

    # Escreve o subcabeçalho da tabela
    modified_subheader = []
    for col in data[1]:
        if "°" in col:
            modified_subheader.append(col.replace("°", "\\textdegree\\hspace{0.25em}"))
        else:
            modified_subheader.append("{" + col + "}")
    for id in modified_subheader:
        tex_file.write("\\multicolumn{1}{c}" + id + " & \n")

    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\\\[0.5ex] \\hline\n")
    tex_file.write("\\\\[-1.8ex]")
    tex_file.write("\n")
    tex_file.write("\n")
    tex_file.write("\\endhead\n")
    tex_file.write("\n")

    tex_file.write("\\multicolumn{3}{l}{\\footnotesize{Continua na próxima página\\ldots}}}\\\\\n")
    tex_file.write("\\endfoot\n")
    tex_file.write("\\hline\n")
    tex_file.write("\n")

    tex_file.write("\\endlastfoot\n")
    tex_file.write("\n")

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
                formatted_row.append("\\num[round-precision=3,round-mode=figures,scientific-notation=true]{" + col + "}")
            else:
                formatted_row.append(col)
        tex_file.write("            " + " & ".join(formatted_row) + " \\\\\n")

    tex_file.write("\\label{tab:dados_terremoto}\n")
    tex_file.write("%\\caption*{Fonte:IPT.}\n")
    tex_file.write("\\end{longtable}\n")
    tex_file.write("\\end{center}\n")
