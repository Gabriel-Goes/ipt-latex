import os

def process_logs(log_files):
    latex_output = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            data = file.readlines()

        # Resumo das informações
        resumo = {
            "Arquivos Processados": None,
            "Arquivos Copiados": None,
            "Arquivos Mesclados": None,
            "Arquivos Sobrepostos": None,
            "Erros": None,
        }

        for line in data:
            if "Tamanho dos arquivos:" in line:
                resumo["Arquivos Processados"] = line.split(":")[-1].strip()
            elif "Arquivos copiados:" in line:
                resumo["Arquivos Copiados"] = line.split(":")[-1].strip()
            elif "Arquivos mesclados:" in line:
                resumo["Arquivos Mesclados"] = line.split(":")[-1].strip()
            elif "Arquivos sobrepostos:" in line:
                resumo["Arquivos Sobrepostos"] = line.split(":")[-1].strip()
            elif "Erros:" in line:
                resumo["Erros"] = line.split(":")[-1].strip()

        latex_output.append(f"""
\\subsection{{Resumo do Log - {log_file}}}
\\begin{{longtable}}{{@{{}}ll@{{}}}}
\\toprule
\\textbf{{Operação}} & \\textbf{{Quantidade}} \\\\ \\midrule
Arquivos Processados & {resumo['Arquivos Processados']} \\\\
Arquivos Copiados    & {resumo['Arquivos Copiados']} \\\\
Arquivos Mesclados   & {resumo['Arquivos Mesclados']} \\\\
Arquivos Sobrepostos & {resumo['Arquivos Sobrepostos']} \\\\
Erros               & {resumo['Erros']} \\\\ \\bottomrule
\\end{{longtable}}
""")
    return latex_output

# Exemplo de uso:
log_folder = '/home/ggrl/projetos/ipt-latex/tex/qc/
latex_sections = process_logs(logs)

# Escrevendo o conteúdo LaTeX em um arquivo:
with open("tex/qc/controle_qualidade_.tex", "w") as tex_file:
    tex_file.write("\n".join(latex_sections))
