def generate_map_latex(output_filename):
    latex_code = r"""
\begin{figure}[hp]
    \centering
	\captionsetup{justification=justified, singlelinecheck=false, width=1\textwidth}
    \caption{Gráficos de completeza dos dados para as estações BC4, BC9 e BC12 durante o período do mês de maio.2023. O registro de todas as estações foi satisfatório durante o período. Para a estação BC4, os últimos dois dias não foram incluídos por problemas na transmissão dos dados para o IPT, entretanto, serão analisados e incluídos no relatório anual. }
    \includegraphics[width=1.0\textwidth]{./boletim/baesa/figuras/bc4_completude.png}
    \includegraphics[width=1.0\textwidth]{./boletim/baesa/figuras/bc9_completude.png}
    \includegraphics[width=1.0\textwidth]{./boletim/baesa/figuras/bc12_completude.png}
    \caption*{Fonte: IPT}
\end{figure}
"""
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)


generate_map_latex("./boletim/baesa/tex/completude_baesa.tex")
