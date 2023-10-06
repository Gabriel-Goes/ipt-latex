import argparse

# Define the possible reservoir names
reservoir_names = {
    "1": "Reservatório de Machadinho, SC/RS",
    "2": "Reservatório de Itá, SC/RS",
    "3": "Reservatório Salto Pilão, RS"
}

# Parse the command-line argument to get the reservoir name
parser = argparse.ArgumentParser(description='Generate Capa_main.tex')
parser.add_argument('reservoir', choices=reservoir_names.keys(),
                    help='Reservoir name (1, 2, or 3)')
args = parser.parse_args()

# Get the selected reservoir name
selected_reservoir = reservoir_names[args.reservoir]

# Generate the LaTeX content with the selected reservoir name
tex_content = f"""\
% Params
\\tipo{{BOLETIM SISMOLÓGICO}}
\\data{{2023}}
\\titulo{{\\textbf{{RSIS - Rede Sismológica Itá/Machadinho}} \\\\
\\textbf{{{selected_reservoir}}} \\\\
\\textbf{{BOLETIM SÍSMICO Nº XXXXXX}}}}
\\unidade{{Cidades Infraestruturas e Meio Ambiente}}{{CIMA}}
\\lab{{Seção de Obras Civis - SOC}}
\\periodo{{MES/ANO}}{{MES/ANO}}

% Inserir capa
\\capa
\\pagestyle{{timbrado}}

\\vspace{{0.5cm}}

\\pagestyle{{geral}}
"""

# Specify the file name and mode ('w' for write)
file_name = "./boletim/main/tex/capa_main_boletim.tex"

# Write the content to the .tex file
with open(file_name, "w") as tex_file:
    tex_file.write(tex_content)

print(f"Created {file_name}")
