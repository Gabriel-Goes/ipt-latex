import os

def generate_latex_for_figures(base_path='files/figures/pos_process/'):
    latex_content = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.png'):
                figure_path = os.path.join(root, file)
                figure_path = '/home/ggrl/projetos/ClassificadorSismologico/' + figure_path
                figure_label = os.path.splitext(file)[0]
                figure_caption = figure_label.replace('_', ' ').capitalize()
                latex_figure = f"""
\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{{{figure_path}}}
    \\caption{{{figure_caption}}}
    \\label{{fig:{figure_label}}}
\\end{{figure}}
"""
                latex_content.append(latex_figure)

    if latex_content:
        print(figure_path)
        with open('source/sismologia-ipt-latex/tex/relatorio_preditivo/tex/figures.tex', 'w') as f:
            f.write('\n'.join(latex_content))
        print("LaTeX file 'figures.tex' has been created successfully.")
    else:
        print("No figures found. No LaTeX file was created.")

generate_latex_for_figures()
