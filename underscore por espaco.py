import os

# Obter o caminho absoluto da pasta atual
path = os.getcwd()

# Percorrer todas as pastas no caminho especificado
for foldername in os.listdir(path):
    # Verificar se o nome da pasta contém um sublinhado
    if "_" in foldername:
        # Obter o novo nome da pasta com espaço em vez de sublinhado
        new_foldername = foldername.replace("_", " ")
        # Renomear a pasta com o novo nome
        os.rename(os.path.join(path, foldername), os.path.join(path, new_foldername))
