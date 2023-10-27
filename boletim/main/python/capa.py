import argparse

# Define the possible reservoir names
reservoir_names = {
    "1": "UHE Machadinho SC/RS",
    "2": "Reservatório de Itá, SC/RS",
    "3": "UHE Salto Pilão, SC"
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

\\titulo{{Estação Sismológica SP7, SC \\\\
          {selected_reservoir} \\\\
          BOLETIM SÍSMICO Nº 26/36-2024 Ago.23 }}

\\unidade{{Cidades Infraestruturas e Meio Ambiente}}{{CIMA}}
\\lab{{Seção de Obras Civis - SOC}}
\\periodo{{01/08/2023}}{{31/08/2023}}

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

print(f" -> Capa '{file_name}' gerada com sucesso!")
