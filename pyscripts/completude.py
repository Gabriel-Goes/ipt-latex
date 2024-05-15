def generate_map_latex(output_filename):
    latex_code = r"""
    \begin{figure}[ht!]
        \centering
        \captionsetup{
        justification=justified, singlelinecheck=false, width=1\
        textwidth}
        \caption{Gráfico de completeza mensal para os dados da estação SP7.
        O detalhamento diário da completeza para cada mês pode ser averiguado
        nos boletins sísmicos mensais no Anexo A.}
        \begin{mdframed}[
            linecolor=black,
            linewidth=1pt,
            roundcorner=10pt,
        ]
        \includegraphics[width=1.0\textwidth]{./relatorio/figuras/completude.png}
        \end{mdframed}
        \caption*{Fonte: IPT}
    \end{figure}
    """
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)
    print(f" -> Figura de completude '{output_filename}' gerada com sucesso!")


generate_map_latex("tex/relatorio_preditivo/tex/completude.tex")
