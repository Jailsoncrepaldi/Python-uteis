import os
import random
import pygame
from pydub import AudioSegment

# pede ao usuário o caminho da pasta com os arquivos de áudio
caminho = "juntar"

# lista todos os arquivos de áudio na pasta
arquivos_audio = [os.path.join(caminho, f) for f in os.listdir(caminho) if f.endswith(".wav") or f.endswith(".mp3")]

# carrega os arquivos de áudio selecionados com o PyDub
audio_junto = AudioSegment.empty()
for arquivo in arquivos_audio:
    audio = AudioSegment.from_file(arquivo)
    audio_junto += audio

# toca o áudio com o Pygame
pygame.mixer.init()
canal = pygame.mixer.Sound(audio_junto.export(format='wav'))
canal.play()

# exporta o áudio para um arquivo MP3 usando o PyDub
caminho_saida = "audio_junto_seq.mp3"
audio_junto.export(caminho_saida, format="mp3")
