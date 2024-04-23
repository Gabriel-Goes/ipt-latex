def generate_map_latex(output_filename):
    latex_code = r"""
\begin{figure}[ht!]
	\captionsetup{justification=justified, singlelinecheck=false, width=1\textwidth}
    \caption{Mapa do entorno do empreendimento mostrando pontos de interesse e os epicentros dos eventos classificados como detonações e sismos. Foram detectados um total de sessenta e sete (67) eventos associados a detonações no período, classificados a partir do horário de ocorrência e da forma de onda, além do plano de fogo fornecido, com magnitudes mínima e máxima de 0.4 e 3.0 MLv, respectivamente.}
    \begin{mdframed}[
        linecolor=black,
        linewidth=1pt,
        roundcorner=10pt,
    ]
    \begin{center}
    \includegraphics[width=0.8\textwidth]{./relatorio/figuras/mapa.png}
    \end{center}
    \end{mdframed}
    \caption*{Fonte: IPT}
\end{figure}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)
    print(f" -> Mapa '{output_filename}' gerado com sucesso!")


generate_map_latex("./relatorio/tex/mapa.tex")
