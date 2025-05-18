import os
import shutil

def organizar_pastas(diretorio_origem):
    # Obtém a lista de pastas no diretório de origem
    pastas_origem = [pasta for pasta in os.listdir(diretorio_origem) if os.path.isdir(os.path.join(diretorio_origem, pasta))]

    # Cria um dicionário para armazenar pastas por quantidade de arquivos
    pastas_por_quantidade = {}

    # Classifica as pastas com base na quantidade de arquivos
    for pasta in pastas_origem:
        caminho_pasta = os.path.join(diretorio_origem, pasta)
        quantidade_arquivos = len(os.listdir(caminho_pasta))

        if quantidade_arquivos not in pastas_por_quantidade:
            pastas_por_quantidade[quantidade_arquivos] = []

        pastas_por_quantidade[quantidade_arquivos].append(caminho_pasta)

    # Cria diretórios de destino e move as pastas
    for quantidade, pastas in pastas_por_quantidade.items():
        diretorio_destino = os.path.join(diretorio_origem, str(quantidade))

        # Cria o diretório de destino se não existir
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)

        # Move as pastas para o diretório de destino
        for pasta in pastas:
            shutil.move(pasta, diretorio_destino)

if __name__ == "__main__":
    # Solicita ao usuário o diretório de origem
    diretorio_origem = input("Digite o caminho do diretório de origem: ")

    # Verifica se o diretório de origem existe
    if os.path.exists(diretorio_origem) and os.path.isdir(diretorio_origem):
        organizar_pastas(diretorio_origem)
        print("Organização concluída com sucesso!")
    else:
        print("O diretório de origem não existe ou não é um diretório válido.")
