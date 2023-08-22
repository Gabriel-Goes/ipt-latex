#!/bin/bash

# Verifica se um argumento foi fornecido
if [ $# -eq 0 ]; then
    echo "Uso: $0 <arquivo.tex>"
    exit 1
fi

# Nome do arquivo LaTeX passado como argumento
input_tex="$1"

# Executa o script Python para gerar o arquivo LaTeX
python ../python/tabela.py

# Gera o arquivo PDF a partir do arquivo LaTeX
pdflatex "$input_tex"

# Remove arquivos temporários gerados pelo pdflatex
rm -f *.aux *.log *.out

echo "Arquivo PDF gerado: ${input_tex%.tex}.pdf"

