def generate_map_latex(output_filename):
    latex_code = r"""
\begin{figure}[ht!]
	\captionsetup{justification=justified, singlelinecheck=false, width=1\textwidth}
    \caption{Evento regional natural registrado em 2023-16-06 11:22:00 (UTC) nas proximidades da cidade de Iguape – SP. A) Localização do evento (círculo vermelho maior) em relação à estação SP7 (círculo vermelho menor) e B) Forma de onda do evento registrada na estação SP7.}

    \begin{mdframed}[
        linecolor=black,
        linewidth=1pt,
        roundcorner=10pt,
    ]
    \textbf{A}
    \begin{center}
    \includegraphics[width=0.8\textwidth]{./relatorio/figuras/regiao.png}
    \end{center}
    \end{mdframed}
    \begin{mdframed}[
        linecolor=black,
        linewidth=1pt,
        roundcorner=10pt,
    ]
    \textbf{B}
    \begin{center}
    \includegraphics[width=0.8\textwidth]{./relatorio/figuras/evento_regional.png}
    \end{center}
    \end{mdframed}

    \caption*{Fonte: IPT}
\end{figure}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)
        print(f" -> Figura de Evento Regional '{output_filename}' gerado com sucesso!")


generate_map_latex("./relatorio/tex/regional.tex")
