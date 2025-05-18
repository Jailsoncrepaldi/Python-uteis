import asyncio
import os
from shazamio import Shazam

def get_unique_filename(directory, filename):
    """
    Gera um nome de arquivo único, adicionando um sufixo numérico se o arquivo já existir no diretório.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1

    return new_filename

async def main():
    shazam = Shazam()

    folder_path = input("Coloque aqui o endereço da pasta onde estão as músicas: ")
    if not os.path.isdir(folder_path):
        print("Caminho da pasta inválido. Por favor, tente novamente.")
        return

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                try:
                    # Reconhecendo a música
                    out = await shazam.recognize(file_path)

                    # Extraindo informações da música
                    artist = out['track'].get('subtitle', 'None')
                    title = out['track'].get('title', 'Unknown Title')

                    if artist == 'None':
                        print(f"Artista não encontrado para {filename}. Arquivo ignorado.")
                        continue

                    # Criando a pasta do artista
                    artist_folder = os.path.join(folder_path, artist)
                    os.makedirs(artist_folder, exist_ok=True)

                    # Criando um novo nome de arquivo único
                    _, file_extension = os.path.splitext(filename)
                    new_filename = f"{artist}-{title}{file_extension}"
                    unique_filename = get_unique_filename(artist_folder, new_filename)

                    # Movendo o arquivo para a pasta do artista
                    new_file_path = os.path.join(artist_folder, unique_filename)
                    os.rename(file_path, new_file_path)

                    print(f"Arquivo {filename} movido para {new_file_path}.")
                except KeyError:
                    print(f"Informações não encontradas para {filename}. Indo para o próximo arquivo.")
                except Exception as e:
                    print(f"Erro ao processar {filename}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
