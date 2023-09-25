import os
import json

# Caminho raíz
base = "/tmp/ValeTeste"
arquivorelatorio = "/tmp/destino/"

# Função para contar arquivos por subdiretório
def contaArquivos(caminho):
    results = {}
    # Preenche o dicionário usando os.walk, relpath e len criando uma chave para cada diretorio com a quantidade de arquivos LEN
    for subdir, dirs, files in os.walk(caminho):
        arquivos = len(files)
        # Cria uma chave para cada subdir os.walk ;)
        results[subdir] = arquivos
    return results


# Loop para fazer por subdiretorio na primeira (anos)
for dir in os.listdir(base):
    # Completa o caminho completo para o os.walk
    caminho = os.path.join(base, dir)
    # Cria um dicionário com a função contaArquivos
    dicionario = contaArquivos(caminho)
    # Cria uma lista de dicionários com os items do dicionário criado anteriormente
    conteudo = [{"{#DIRNAME}":subdir, "{#DIRLEN}": arquivos} for subdir, arquivos in dicionario.items()]
    # Converte tudo para json
    toJson = json.dumps(conteudo, indent=2)
    # Exportar JSON
    # Arquivo
    resultado = arquivorelatorio + dir + ".json"
    with open(resultado, "w") as f:
        f.write(toJson)