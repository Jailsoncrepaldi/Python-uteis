import os
import subprocess

# Nome da pasta onde os áudios acelerados serão salvos
output_folder = "audios_2x"
os.makedirs(output_folder, exist_ok=True)  # Cria a pasta se não existir

def speed_up_audio_ffmpeg(input_file, output_file, speed=2.0):
    """Acelera o áudio sem cortar partes usando ffmpeg e o filtro atempo."""
    command = [
        "ffmpeg", "-i", input_file, "-filter:a",
        f"atempo={speed}", "-vn", output_file
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Pega todos os arquivos MP3 na pasta atual
mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]

for file in mp3_files:
    print(f"Processando: {file}")
    
    # Caminho completo para salvar o novo arquivo na pasta de saída
    new_file = os.path.join(output_folder, f"2x_{file}")
    
    # Aplicar a aceleração
    speed_up_audio_ffmpeg(file, new_file, speed=2.0)
    
    print(f"Arquivo salvo em: {new_file}")

print(f"Processamento concluído! Arquivos acelerados estão na pasta '{output_folder}'.")
