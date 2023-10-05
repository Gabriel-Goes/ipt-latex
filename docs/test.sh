#!/bin/bash

# Solicita ao usuário que selecione uma opção
echo "Selecione a opção desejada:"
echo "1 - Machadinho"
echo "2 - Baesa"
read opcao
## Verifica a opção escolhida e executa os arquivos correspondentes
if [ "$opcao" == "1" ]; then
    tabela=~/projetos/ipt-latex/boletim/machadinho/python/tabela.py
    mapa=~/projetos/ipt-latex/boletim/machadinho/python/mapa_machadinho.py
    input_tex=~/projetos/ipt-latex/boletim/machadinho/machadinho_boletim.tex

    # Verifica se os arquivos existem antes de executá-los
    #[ -f "$tabela" ] && [ -f "$mapa" ] && 
    #
    if [ -f $"input_tex" ]; then
        echo "$input_tex"
    else
        if [ 1 == 1 ]; then
            echo "1 = 1"
        else
            echo "1 diferente de 1"
        fi
    
    fi

    if [ -f "$input_tex" ]; then
        echo "Executando os scripts Python"
        python3 "$tabela"
        python3 "$mapa"
    else
        echo "Um ou mais scripts Python não encontrados"
        exit 1
    fi
fi
