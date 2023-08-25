def generate_latex_code(output_filename):
    latex_code = r"""
\begin{figure}[h]
    \centering
    \caption{Gráfico de completude dos dados para o mês de XXX para estação XXX.}
    \includegraphics[width=1.0\textwidth]{../figuras/completude.png} % Substitua pelo nome da imagem e ajuste o tamanho
    \caption*{Fonte:IPT}
\end{figure}
""" 
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)

# Substitua "completude.png" pelo nome da sua imagem e "completude.tex" pelo nome desejado para o arquivo de saída
generate_latex_code("../tex/Completude.tex")
