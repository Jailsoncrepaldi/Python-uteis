import os
from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import detect_nonsilent

def list_audio_files():
    """Lista todos os arquivos de áudio na pasta atual."""
    files = [f for f in os.listdir('.') if f.endswith(('.mp3', '.wav'))]
    return files

def select_file(files, prompt):
    """Exibe um menu para selecionar um arquivo."""
    print(prompt)
    for idx, file in enumerate(files, start=1):
        print(f"{idx}: {file}")
    while True:
        try:
            choice = int(input("Escolha o número do arquivo: "))
            if 1 <= choice <= len(files):
                return files[choice - 1]
        except ValueError:
            pass
        print("Escolha inválida, tente novamente.")

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


def main():
    files = list_audio_files()
    if not files:
        print("Nenhum arquivo de áudio encontrado na pasta.")
        return

    narration_file = select_file(files, "Selecione o arquivo de narração:")
    background_file = select_file(files, "Selecione o arquivo de fundo:")

    print("Carregando arquivos...")
    narration = AudioSegment.from_file(narration_file)
    background = AudioSegment.from_file(background_file)

    # Ajustar o fundo para o comprimento da narração
    while len(background) < len(narration):
        background += background  # Repetir o fundo

    background = background[:len(narration)]  # Ajustar ao tamanho exato da narração

    print("Aplicando efeito de Auto Duck...")
    mixed_audio = auto_duck(narration, background)

    output_file = "saida_mixada.mp3"  # Gera diretamente em MP3
    mixed_audio.export(output_file, format="mp3", bitrate="192k")
    print(f"Arquivo mixado salvo como: {output_file}")


if __name__ == "__main__":
    main()
