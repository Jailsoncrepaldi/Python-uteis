import os

def create_folders():
    # Solicita ao usuário um número
    num = int(input("Digite um número: "))

    # Determina o número de dígitos necessário para os nomes das pastas
    num_digits = len(str(num))

    # Cria as pastas com o nome correto
    for i in range(1, num + 1):
        folder_name = str(i).zfill(num_digits)
        os.makedirs(folder_name, exist_ok=True)
        print(f'Pasta "{folder_name}" criada.')

if __name__ == "__main__":
    create_folders()
