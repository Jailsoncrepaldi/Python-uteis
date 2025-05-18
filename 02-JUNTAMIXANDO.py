import os
from tkinter import filedialog, Tk
from pydub import AudioSegment

def selecionar_pasta():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    pasta = filedialog.askdirectory(title="Selecione a pasta com os arquivos MP3")
    return pasta

def juntar_audios(pasta_entrada):
    # Localize arquivos MP3 na pasta
    audios = [f for f in os.listdir(pasta_entrada) if f.endswith('.mp3')]

    if len(audios) < 2:
        print("É necessário pelo menos dois arquivos MP3 para juntar.")
        return

    # Carregar os dois primeiros arquivos de áudio
    audio1 = AudioSegment.from_mp3(os.path.join(pasta_entrada, audios[0]))
    audio2 = AudioSegment.from_mp3(os.path.join(pasta_entrada, audios[1]))

    # Misturar os dois áudios
    combinado = audio1.overlay(audio2)

    # Salvar o áudio combinado na mesma pasta do script
    arquivo_saida = "audio_combinado.mp3"
    combinado.export(arquivo_saida, format="mp3")
    print(f"Áudio combinado salvo como {arquivo_saida} na pasta do script.")

if __name__ == "__main__":
    pasta_entrada = selecionar_pasta()
    if pasta_entrada:
        juntar_audios(pasta_entrada)
