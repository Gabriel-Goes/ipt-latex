def generate_map_latex(output_filename):
    latex_code = r"""
\section{MAPA DE EVENTOS}
\begin{figure}[h]
    \centering
    \caption{Mapa de eventos.}
    \includegraphics[width=1.0\textwidth]{mapaevents.png} % Substitua pelo nome do arquivo de imagem e ajuste o tamanho
    \caption*{Fonte:IPT}
\end{figure}
""" % image_filename

    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)

# Substitua "mapaevento.png" pelo nome da sua imagem e "Mapa.tex" pelo nome desejado para o arquivo de saída
generate_map_latex( "Mapa.tex")

