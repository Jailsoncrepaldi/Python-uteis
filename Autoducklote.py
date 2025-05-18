import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def list_audio_files(folder):
    """Lista todos os arquivos de áudio em uma pasta específica."""
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.mp3', '.wav'))]

def auto_duck(narration, background, duck_amount=-70, attack=200, decay=200):
    """
    Aplica o efeito de auto duck no áudio de fundo com base na narração.
    - duck_amount: Redução de volume do fundo (em dB).
    - attack e decay: Tempos de ataque e recuperação (em ms).
    """
    # Reduz o volume base do fundo
    background = background - 20  # Reduzir volume geral do fundo
    
    output = AudioSegment.silent(duration=len(narration))
    nonsilent_ranges = detect_nonsilent(narration, min_silence_len=50, silence_thresh=-40)

    for start, end in nonsilent_ranges:
        # Trecho do fundo correspondente à narração
        bg_segment = background[start:end]
        # Aplica redução de volume extrema
        bg_segment = bg_segment + duck_amount
        # Mistura o fundo reduzido na saída
        output = output.overlay(bg_segment, position=start)

    # Completa os espaços com o fundo ajustado
    remaining_background = background.overlay(output, loop=True)[:len(narration)]
    return remaining_background.overlay(narration)

def process_one_to_one():
    narration_folder = "narracoes"
    background_folder = "fundos"
    output_folder = "saidas"

    # Garantir que as pastas existem
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    narrations = sorted(list_audio_files(narration_folder))
    backgrounds = sorted(list_audio_files(background_folder))

    if not narrations:
        print("Nenhuma narração encontrada na pasta 'narracoes'.")
        return

    if not backgrounds:
        print("Nenhum fundo encontrado na pasta 'fundos'.")
        return

    if len(narrations) != len(backgrounds):
        print("A quantidade de narrações e fundos não é igual. Usando os pares disponíveis.")

    for narration_path, background_path in zip(narrations, backgrounds):
        narration_name = os.path.splitext(os.path.basename(narration_path))[0]
        background_name = os.path.splitext(os.path.basename(background_path))[0]
        narration = AudioSegment.from_file(narration_path)
        background = AudioSegment.from_file(background_path)

        # Ajustar o fundo para o comprimento da narração
        while len(background) < len(narration):
            background += background  # Repetir o fundo

        background = background[:len(narration)]  # Ajustar ao tamanho exato da narração

        print(f"Processando: {narration_name} com {background_name}")
        mixed_audio = auto_duck(narration, background)

        # Nome do arquivo de saída
        output_file = os.path.join(output_folder, f"{narration_name}.mp3")
        mixed_audio.export(output_file, format="mp3", bitrate="192k")
        print(f"Arquivo salvo: {output_file}")

if __name__ == "__main__":
    process_one_to_one()
