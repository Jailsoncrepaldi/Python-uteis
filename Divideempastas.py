import os
import shutil

def criar_pastas(destino, num_pastas):
    for i in range(1, num_pastas + 1):
        pasta = os.path.join(destino, f"{i:02}")
        os.makedirs(pasta, exist_ok=True)

def organizar_arquivos(origem, destino, arquivos_por_pasta):
    # Lista todos os arquivos em todas as subpastas da pasta de origem
    arquivos = []
    for root, _, files in os.walk(origem):
        for file in files:
            arquivos.append(os.path.join(root, file))
    
    total_arquivos = len(arquivos)
    
    # Calcula o número necessário de pastas
    num_pastas = (total_arquivos // arquivos_por_pasta) + (1 if total_arquivos % arquivos_por_pasta != 0 else 0)
    
    # Cria as pastas no destino
    criar_pastas(destino, num_pastas)
    
    # Move os arquivos para as novas pastas
    pasta_atual = 1
    contador = 0
    
    for arquivo in arquivos:
        if contador == arquivos_por_pasta:
            pasta_atual += 1
            contador = 0
        
        pasta_destino = os.path.join(destino, f"{pasta_atual:02}")
        shutil.move(arquivo, os.path.join(pasta_destino, os.path.basename(arquivo)))
        contador += 1

if __name__ == "__main__":
    origem = input("Digite o caminho da pasta de origem: ")
    destino = input("Digite o caminho da pasta de destino: ")
    arquivos_por_pasta = int(input("Digite o número de arquivos por pasta: "))
    
    if not os.path.isdir(origem):
        print("O diretório de origem não existe.")
    elif not os.path.isdir(destino):
        print("O diretório de destino não existe.")
    else:
        organizar_arquivos(origem, destino, arquivos_por_pasta)
        print("Arquivos organizados com sucesso!")
