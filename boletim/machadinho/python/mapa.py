def generate_map_latex(output_filename):
    latex_code = r"""
\begin{figure}[h]
    \centering
    \caption{Mapa de eventos.}
    \includegraphics[width=1.0\textwidth]{./figuras/mapaevents.png}
    \caption*{Fonte:IPT}
\end{figure}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)


generate_map_latex("./tex/mapa_machadinho_boletim.tex")
