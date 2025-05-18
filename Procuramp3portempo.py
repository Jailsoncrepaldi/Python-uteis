import os
import shutil
from mutagen.mp3 import MP3


def remove_caracteres_invalidos(texto):
    texto = texto.replace(" ", "_").strip()
    return texto


def mover_arquivo_com_contador(origem, destino):
    contador = 1
    nome_arquivo, extensao = os.path.splitext(os.path.basename(origem))
    novo_nome_arquivo = nome_arquivo

    while os.path.exists(os.path.join(destino, novo_nome_arquivo + extensao)):
        novo_nome_arquivo = f"{nome_arquivo}_{contador}"
        contador += 1

    shutil.move(origem, os.path.join(destino, novo_nome_arquivo + extensao))


def criar_pasta(destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    return destino


def processar_pasta_por_duracao(pasta_origem, tempo_em_segundos):
    pasta_destino = criar_pasta(os.path.join(pasta_origem, f"Duração_{tempo_em_segundos}s"))
    
    for root, _, files in os.walk(pasta_origem):
        for arquivo in files:
            if arquivo.endswith(".mp3"):
                caminho_arquivo = os.path.join(root, arquivo)
                try:
                    audio = MP3(caminho_arquivo)
                    duracao = int(audio.info.length)

                    if duracao == tempo_em_segundos:
                        mover_arquivo_com_contador(caminho_arquivo, pasta_destino)
                        print(f"Arquivo movido: {arquivo}")
                except Exception as e:
                    print(f"Erro ao processar o arquivo {caminho_arquivo} {arquivo}: {e}")
    
    print(f"Arquivos com duração de {tempo_em_segundos} segundos organizados na pasta: {pasta_destino}")


def main():
    print("Organizador de MP3 por Duração")
    pasta_origem = os.getcwd()
    try:
        tempo_em_segundos = int(input("Digite o tempo de duração em segundos para classificar os arquivos MP3: "))
        processar_pasta_por_duracao(pasta_origem, tempo_em_segundos)
    except ValueError:
        print("Por favor, insira um número válido para o tempo em segundos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
