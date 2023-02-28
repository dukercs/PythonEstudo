import os
import json

# Caminho raíz
base = "/tmp/ValeTeste"

# Função para contar arquivos por subdiretório
def count_files_by_subdir(base):
    # Cria um dicionário vazio
    results = {}
    # Preenche o dicionário usando os.walk e relpath
    for root, dirs, files in os.walk(base):
        subdir = os.path.relpath(root, base)
        # Preenche o dicionário
        results.setdefault(subdir, len(files))
    return results


conteudo = count_files_by_subdir(base)

# Exportar JSON
json_formatado = json.dumps(conteudo, indent=2)
print(json_formatado)
