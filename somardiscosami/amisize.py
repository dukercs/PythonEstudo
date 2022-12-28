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

for i in range(len(dados)):
    print(dados[i]["Origem"], end = ' - ')
    for d in range(len(dados[i]["Discos"])):
        tamanho = dados[i]["Discos"][d]
        somatamanho += tamanho
    print("Tamanho total dos discos na AMI: {} GB".format(somatamanho), end = ' ')
    totaldiscos  += somatamanho
    somatamanho = 0
    print(" ")
print("Total nesse arquivo: {} GB".format(totaldiscos))



# for data in dados:
#      for x in data:
#         print(x)
