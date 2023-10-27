def generate_map_latex(output_filename):
    latex_code = r"""
    \begin{figure}[ht!]
    \centering
    \captionsetup{justification=justified, singlelinecheck=false, width=1\textwidth}
    \caption{Mapa da região de interesse no entorno do empreendimento, mostrando as principais cidades, rodovias e rios, com a localização das pedreiras, estações \textbf{BCM2} e \textbf{MC9}, e eventos próximos ao empreendimento detectados no período de interesse.}
    \includegraphics[width=1.0\textwidth]{./boletim/main/figuras/mapaevents.png}
    \caption*{Fonte: IPT}
    \end{figure}
    \newpage
    """
    with open(output_filename, "w") as output_file:
        output_file.write(latex_code)

    print(f" -> Mapa '{output_filename}' gerado com sucesso!")


generate_map_latex("./boletim/main/tex/mapa_main_boletim.tex")
