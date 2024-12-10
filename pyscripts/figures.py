import os
import argparse

HOME = os.getenv('HOME')
PROJ = HOME+'/projetos/ClassificadorSismologico/'

# Function to generate LaTeX code for figures
# Recebe o a pasta que contem imagens.png e retorna um figuras.tex.
# Onde cada figura é um ambiente figure com a imagem e a legenda base.

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    '--path',
    help='Path to the folder containing the images',
    required=True
)
args = arg_parser.parse_args()


def generate_latex_for_figures(path=args.path):
    latex_content = []
    base_path = os.path.abspath(f'{PROJ}arquivos/figuras/{path}')
    print(base_path)

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.png'):
                figure_path = os.path.join(root, file)
                figure_label = os.path.splitext(file)[0]
                figure_caption = figure_label.replace('_', ' ').capitalize()
                latex_figure = f"""
    \\begin{{figure}}[H]
        \\centering
        \\includegraphics[width=1.0\\textwidth]{{{figure_path}}}
        \\caption{{{figure_caption}}}
        \\label{{fig:{figure_label}}}
    \\end{{figure}}
                """
                latex_content.append(latex_figure)

    if latex_content:
        figures_tex_path = f'{PROJ}fonte/relatorio-sismologia/tex/relatorio_preditivo/tex/{args.path}_figures.tex'
        with open(figures_tex_path, 'w') as f:
            f.write('\n'.join(latex_content))
        print(
            f"LaTeX file '{figures_tex_path}' has been created successfully."
        )
    else:
        print("No figures found. No LaTeX file was created.")


if __name__ == '__main__':
    generate_latex_for_figures(path=args.path)
