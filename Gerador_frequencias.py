import os
import numpy as np
import wave
from scipy import signal

def escrever_arquivos_frequencias(forma_onda, pasta_destino, duracao, finicial, ffinal, passo=1):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    frequencias = np.arange(finicial, ffinal + 1, passo)  # Frequências
    amplitude_maxima = 32767  # Amplitude máxima

    for indice, frequencia in enumerate(frequencias):
        contador = indice + 1

        # Gerar arquivo para cada frequência individual
        nome_arquivo_frequencia = f'frequencia_{frequencia}Hz.wav'
        caminho_arquivo_frequencia = os.path.join(pasta_destino, nome_arquivo_frequencia)

        taxa_amostragem = 44100  # Taxa de amostragem em Hz

        tempo = np.linspace(0, duracao, int(duracao * taxa_amostragem), endpoint=False)

        if forma_onda == '1':
            sinal = amplitude_maxima * np.sin(2 * np.pi * frequencia * tempo)
        elif forma_onda == '2':
            sinal = amplitude_maxima * np.sign(np.sin(2 * np.pi * frequencia * tempo))
        elif forma_onda == '3':
            sinal = amplitude_maxima * signal.sawtooth(2 * np.pi * frequencia * tempo)

        sinal = sinal.astype(np.int16)

        # Gravar arquivo para a frequência individual
        arquivo_frequencia = wave.open(caminho_arquivo_frequencia, 'w')
        arquivo_frequencia.setnchannels(1)  # Configuração para áudio mono
        arquivo_frequencia.setsampwidth(2)  # Configuração para dados de 16 bits
        arquivo_frequencia.setframerate(taxa_amostragem)  # Configuração da taxa de amostragem
        arquivo_frequencia.writeframes(sinal.tobytes())
        arquivo_frequencia.close()


forma_onda = input("Digite a forma de onda desejada (1 - seno, 2 - quadrada, 3 - dente-de-serra): ")
pasta_destino = input("Digite o caminho completo da pasta de destino: ")
duracao = float(input("Digite a duração do audio em segundos: "))
finicial = int(input("Digite a frequência inicial: "))
ffinal = int(input("Digite a frequência final: "))
passo = int(input("Digite o valor do passo: "))

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

escrever_arquivos_frequencias(forma_onda, pasta_destino, duracao, finicial, ffinal, passo)
