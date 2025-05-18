from pydub import AudioSegment
import os

def convert_to_mono_22050hz(input_folder, output_folder):
    # Verifica se a pasta de saída existe, senão cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos os arquivos na pasta de entrada
    files = os.listdir(input_folder)
    
    for file in files:
        if file.endswith(".wav"):  # Verifica se é um arquivo WAV
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)
            
            # Carrega o arquivo de áudio
            sound = AudioSegment.from_wav(input_path)


            # Converte para mono e 22050 Hz
            sound = sound.set_frame_rate(22050).set_channels(1)

            # Salva o arquivo convertido
            sound.export(output_path, format="wav")
            print(f"{file} convertido com sucesso.")

# Pede ao usuário o caminho da pasta de entrada
input_folder = input("Digite o caminho da pasta onde estão os arquivos WAV: ")

# Pede ao usuário o caminho da pasta de saída
output_folder = input("Digite o caminho da pasta de saída para os arquivos convertidos: ")

# Chama a função para converter os arquivos
convert_to_mono_22050hz(input_folder, output_folder)
