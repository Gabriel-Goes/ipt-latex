import os
HOME = os.getenv('HOME')
PROJ = HOME+'/projetos/ClassificadorSismologico/'


def generate_latex_for_figures():
    latex_content = []
    base_path = os.path.abspath(PROJ+'arquivos/figuras/pos_processo/')
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
        figures_tex_path = os.path.join(
            PROJ+'fonte',
            'sismologia-ipt-latex',
            'tex',
            'relatorio_preditivo',
            'tex',
            'figures.tex'
        )
        with open(figures_tex_path, 'w') as f:
            f.write('\n'.join(latex_content))
        print(
            f"LaTeX file '{figures_tex_path}' has been created successfully."
        )
    else:
        print("No figures found. No LaTeX file was created.")


if __name__ == '__main__':
    generate_latex_for_figures()
