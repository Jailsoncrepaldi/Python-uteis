import os

def renomear_arquivos(diretorio, inicial):
    arquivos = sorted(os.listdir(diretorio))  # Ordena os arquivos
    contador = inicial

    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1]  # Obtém a extensão do arquivo
        if extensao.lower() == ".mp3":  # Verifica se é um arquivo MP3
            while True:  # Tenta encontrar um nome válido
                novo_nome = f"{contador:03}{extensao}"  # Formata o número com 3 dígitos e mantém a extensão
                caminho_novo = os.path.join(diretorio, novo_nome)

                if not os.path.exists(caminho_novo):  # Verifica se o nome já existe
                    caminho_antigo = os.path.join(diretorio, arquivo)
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {arquivo} -> {novo_nome}")
                    contador += 1
                    break  # Sai do loop ao renomear com sucesso
                else:
                    contador += 1  # Incrementa o número se o nome já existir

if __name__ == "__main__":
    diretorio = os.getcwd()  # Define o diretório como o atual
    inicial = int(input("Digite o número inicial: "))
    renomear_arquivos(diretorio, inicial)
