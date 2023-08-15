#!/bin/bash
# Verifica se o número de argumentos é válido
if [ $# -ne 1 ]; then
    echo "Uso: $0 <arquivo.csv>"
    exit 1
fi

# Armazena o nome do arquivo CSV
arquivo_entrada="$1"
arquivo_saida="${arquivo_entrada%.csv}_virgulas.csv"

# Verifica se o arquivo de entrada existe
if [ ! -f "$arquivo_entrada" ]; then
    echo "O arquivo $arquivo_entrada não existe."
    exit 1
fi

# Substitui os ponto-e-vírgulas por vírgulas e salva em um novo arquivo
sed 's/;/,/g' "$arquivo_entrada" > "$arquivo_saida"

echo "Conversão concluída. Resultado salvo em $arquivo_saida"

