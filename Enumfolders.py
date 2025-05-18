import os

def renomear_pastas(diretorio, inicial):
    pastas = sorted([pasta for pasta in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, pasta))])  # Filtra apenas pastas

    contador = inicial

    for pasta in pastas:
        novo_nome = f"{contador:03}"  # Formata o número com 3 dígitos

        caminho_antigo = os.path.join(diretorio, pasta)
        caminho_novo = os.path.join(diretorio, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {pasta} -> {novo_nome}")

        contador += 1

if __name__ == "__main__":
    diretorio = os.getcwd()  # Define o diretório como o atual
    inicial = int(input("Digite o número inicial: "))

    renomear_pastas(diretorio, inicial)
