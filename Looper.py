import os
import pydub

input_file = input("Digite o nome do arquivo de entrada (mp3 ou wav): ")
output_time = int(input("Digite o tempo desejado do arquivo de saída em segundos: "))
output_format = input("Digite o formato desejado do arquivo de saída (mp3 ou wav): ")

# Verifica se o arquivo de entrada existe
if not os.path.exists(input_file):
    print("Arquivo de entrada não encontrado.")
    exit()

# Lê o arquivo de entrada
audio = pydub.AudioSegment.from_file(input_file)

# Calcula quantas vezes o arquivo de entrada deve ser repetido
repeat_count = int(output_time / (len(audio) / 1000))
output_audio = audio * repeat_count

# Define o nome do arquivo de saída
output_file = f"output.{output_format}"

# Exporta o arquivo de saída
if output_format == "mp3":
    output_audio.export(output_file, format="mp3")
else:
    output_audio.export(output_file, format="wav")

print(f"Arquivo {output_file} criado com sucesso!")
