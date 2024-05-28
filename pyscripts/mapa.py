import os
HOME = os.getenv('HOME')
PROJ = HOME+'/projetos/ClassificadorSismologico/'


def generate_map_latex(base_path, output_filename):
    map_image_path = os.path.join(base_path, 'arquivos/figuras/mapas/mapa.png')
    latex_code = rf"""
\begin{{figure}}[ht!]
	\captionsetup{{justification=justified, singlelinecheck=false, width=1\textwidth}}
    \caption{{Mapa do Brasil mostrando pontos de interesse e os epicentros dos eventos classificados como detonações e sismos. Foram detectados um total de sessenta e sete (67) eventos associados a detonações no período, classificados a partir do horário de ocorrência e da forma de onda, além do plano de fogo fornecido, com magnitudes mínima e máxima de 0.4 e 3.0 MLv, respectivamente.}}
    \begin{{mdframed}}[
        linecolor=black,
        linewidth=1pt,
        roundcorner=10pt,
    ]
    \begin{{center}}
    \includegraphics[width=0.8\textwidth]{{{map_image_path}}}
    \end{{center}}
    \end{{mdframed}}
    \caption*{{Fonte: IPT}}
\end{{figure}}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)
    print(f" -> Mapa '{output_filename}' gerado com sucesso!")


base_path = os.path.abspath(PROJ)
generate_map_latex(
    base_path,
    os.path.join(
        base_path,
        "fonte/relatorios-sismologia/tex/relatorio_preditivo/tex/mapa.tex"
    )
)
