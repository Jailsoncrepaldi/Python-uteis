import os
import pygame
from pydub import AudioSegment

# Pede ao usuário o caminho das pastas com os arquivos de áudio
caminho_pasta1 = "pasta1"
caminho_pasta2 = "pasta2"

# Lista todos os arquivos de áudio nas pastas
arquivos_pasta1 = [os.path.join(caminho_pasta1, f) for f in os.listdir(caminho_pasta1) if f.endswith(".wav") or f.endswith(".mp3")]
arquivos_pasta2 = [os.path.join(caminho_pasta2, f) for f in os.listdir(caminho_pasta2) if f.endswith(".wav") or f.endswith(".mp3")]

# Ordena os arquivos alfabeticamente
arquivos_pasta1.sort()
arquivos_pasta2.sort()

# Verifica se o número de arquivos nas pastas é igual
if len(arquivos_pasta1) != len(arquivos_pasta2):
    print("O número de arquivos nas pastas não é o mesmo. Não é possível unir os pares.")
    exit()

# Cria a pasta de saída, se não existir
pasta_saida = "audio_junto_seq"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# Unir os pares de arquivos
for arquivo1, arquivo2 in zip(arquivos_pasta1, arquivos_pasta2):
    nome_arquivo1 = os.path.basename(arquivo1)
    nome_arquivo2 = os.path.basename(arquivo2)
    nome_arquivo_final = nome_arquivo2  # Nome do arquivo final é baseado no arquivo da pasta 2

    # Carrega os arquivos de áudio selecionados com o PyDub
    audio1 = AudioSegment.from_file(arquivo1)
    audio2 = AudioSegment.from_file(arquivo2)
    audio_junto = audio1 + audio2

    # Toca o áudio com o Pygame
    pygame.mixer.init()
    canal = pygame.mixer.Sound(audio_junto.export(format='wav'))


    # Exporta o áudio para um arquivo MP3 usando o PyDub
    caminho_saida = os.path.join(pasta_saida, nome_arquivo_final)
    audio_junto.export(caminho_saida, format="mp3")
