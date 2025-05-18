import os
import shutil
from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen.mp3 import MP3
import re


def remove_caracteres_invalidos(texto):
    texto = re.sub(r'[<>:"/\\|?*]', '', texto)
    texto = texto.strip()
    texto = texto.replace(" ", "_")
    return texto


def mover_arquivo_com_contador(origem, destino):
    contador = 1
    nome_arquivo, extensao = os.path.splitext(os.path.basename(origem))
    novo_nome_arquivo = nome_arquivo

    while os.path.exists(os.path.join(destino, novo_nome_arquivo + extensao)):
        novo_nome_arquivo = f"{nome_arquivo}_{contador}"
        contador += 1

    shutil.move(origem, os.path.join(destino, novo_nome_arquivo + extensao))


def criar_pasta_hierarquica(base_dir, atributos):
    for atributo in atributos:
        base_dir = os.path.join(base_dir, atributo)
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
    return base_dir


def processar_arquivo(caminho_arquivo, atributos_escolhidos):
    try:
        # Inicializa os atributos com valores padrão
        atributos = {
            "Artista": "Desconhecido",
            "Álbum": "Desconhecido",
            "Ano": "Desconhecido",
            "Nome": "Desconhecido",
            "Número da Faixa": "Desconhecido",
            "Artista Participante": "Desconhecido",
            "Gênero": "Desconhecido",
            "Duração": "Desconhecido",
            "Taxa de Bits": "Desconhecido",
            "Frequência": "Desconhecido",
        }

        # Tenta ler as tags ID3
        try:
            tags = ID3(caminho_arquivo)
            atributos.update({
                "Artista": tags.get("TPE1"),
                "Álbum": tags.get("TALB"),
                "Ano": tags.get("TDRC"),
                "Nome": tags.get("TIT2"),
                "Número da Faixa": tags.get("TRCK"),
                "Artista Participante": tags.get("TPE2") or tags.get("TPE1"),
                "Gênero": tags.get("TCON"),
            })
        except ID3NoHeaderError:
            pass  # Continua mesmo se não houver cabeçalho ID3

        # Tenta ler informações do arquivo de áudio
        audio = MP3(caminho_arquivo)
        atributos.update({
            "Duração": f"{int(audio.info.length // 60)}min_{int(audio.info.length % 60)}s",
            "Taxa de Bits": f"{audio.info.bitrate // 1000}kbps",
            "Frequência": f"{audio.info.sample_rate}Hz",
        })

        # Prepara a lista de valores dos atributos
        valores_atributos = []
        for atributo in atributos_escolhidos:
            valor = atributos.get(atributo)
            valor_atributo = str(valor) if valor else "None"
            valor_atributo = remove_caracteres_invalidos(valor_atributo)
            valores_atributos.append(valor_atributo)

        # Cria a pasta de destino e move o arquivo
        pasta_destino = criar_pasta_hierarquica(pasta_atual, valores_atributos)
        mover_arquivo_com_contador(caminho_arquivo, pasta_destino)

    except Exception as e:
        print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")


def processar_pasta(pasta_atual, atributos_escolhidos):
    for root, _, files in os.walk(pasta_atual):
        for arquivo in files:
            if arquivo.endswith(".mp3"):
                caminho_arquivo = os.path.join(root, arquivo)
                processar_arquivo(caminho_arquivo, atributos_escolhidos)


def tirapastasvazias(diretorio):
    for root, dirs, _ in os.walk(diretorio, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


def exibir_menu():
    print("\nMenu:")
    print("1. Classificar por Artista")
    print("2. Classificar por Álbum")
    print("3. Classificar por Ano")
    print("4. Classificar por Nome")
    print("5. Classificar por Número da Faixa")
    print("6. Classificar por Artista Participante")
    print("7. Classificar por Gênero")
    print("8. Classificar por Duração")
    print("9. Classificar por Taxa de Bits")
    print("10. Classificar por Frequência")
    print("11. Classificar por múltiplos atributos")
    print("12. Sair")


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "12":
            break

        atributos_map = {
            "1": ["Artista"],
            "2": ["Álbum"],
            "3": ["Ano"],
            "4": ["Nome"],
            "5": ["Número da Faixa"],
            "6": ["Artista Participante"],
            "7": ["Gênero"],
            "8": ["Duração"],
            "9": ["Taxa de Bits"],
            "10": ["Frequência"],
            "11": ["Artista", "Álbum", "Ano", "Nome", "Número da Faixa", "Artista Participante", "Gênero", "Duração", "Taxa de Bits", "Frequência"],
        }

        atributos_escolhidos = atributos_map.get(escolha)
        if atributos_escolhidos:
            print(f"\nClassificando músicas por: {', '.join(atributos_escolhidos)}\n")
            processar_pasta(pasta_atual, atributos_escolhidos)
            tirapastasvazias(pasta_atual)
            print("Músicas classificadas e organizadas com sucesso.")
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    pasta_atual = os.getcwd()
    main()
