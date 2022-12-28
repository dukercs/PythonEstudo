import json
import sys
somatamanho = 0
totaldiscos = 0
if len(sys.argv) < 2:
    print("Use {} nome_do_arquivo_json".format(sys.argv[0]))
    exit(2)
arquivo=sys.argv[1]

print("Arquivo: {}".format(arquivo))

with open(arquivo, 'r') as arquivoAberto:
    dados = json.load(arquivoAberto)

print(type(dados))

for linhas in dados:
    # print(dados[linhas])
    print("Imagem criada em {} a partir de {}".format(dados[linhas]["CreationDate"], dados[linhas]["ImageLocation"]))