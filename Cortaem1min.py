from pydub import AudioSegment
import os

def arquivo_ja_processado(output_base_folder, arquivo_original):
    """
    Verifica se algum arquivo de saída já existe no diretório base de saída.
    """
    print(f"Verificando se '{arquivo_original}' já foi processado...")
    nome_base = os.path.splitext(arquivo_original)[0]
    for root, _, files in os.walk(output_base_folder):
        for file in files:
            if file.startswith(nome_base) and file.endswith('.mp3'):
                print(f"Encontrado arquivo processado correspondente: {os.path.join(root, file)}")
                return True
    print(f"'{arquivo_original}' ainda não foi processado.")
    return False

def cortar_arquivos_mp3(input_folder, output_base_folder, duracao_minuto=1):
    # Listar todos os arquivos MP3 na pasta de entrada
    arquivos_mp3 = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]

    if not arquivos_mp3:
        print("Nenhum arquivo MP3 encontrado na pasta de entrada.")
        return

    print(f"Encontrados {len(arquivos_mp3)} arquivos MP3 para processar.")
    for arquivo in arquivos_mp3:
        print(f"\nProcessando arquivo: {arquivo}")

        # Verificar se o arquivo já foi processado em qualquer pasta de saída
        if arquivo_ja_processado(output_base_folder, arquivo):
            print(f"Pulando arquivo '{arquivo}' porque já foi processado.")
            continue

        # Criar pasta de saída com o nome do arquivo (sem extensão)
        output_folder = os.path.join(output_base_folder, os.path.splitext(arquivo)[0])
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Criada pasta de saída: {output_folder}")
        else:
            print(f"Pasta de saída já existe: {output_folder}")

        # Caminho do arquivo de entrada
        input_file = os.path.join(input_folder, arquivo)

        # Carregar o arquivo MP3
        print(f"Carregando arquivo MP3: {input_file}")
        audio = AudioSegment.from_mp3(input_file)

        # Converter a duração desejada para milissegundos
        duracao_milissegundos = duracao_minuto * 60 * 1000

        # Iniciar o índice de corte
        index = 0
        parte_numero = 1

        while index < len(audio):
            # Definir o nome do arquivo de saída
            output_file = os.path.join(output_folder, f"parte_{parte_numero}.mp3")

            # Cortar o áudio
            print(f"Cortando parte {parte_numero}...")
            parte = audio[index:index + duracao_milissegundos]

            # Salvar a parte como um novo arquivo
            print(f"Salvando parte {parte_numero} em: {output_file}")
            parte.export(output_file, format="mp3")

            # Atualizar o índice e o número da parte
            index += duracao_milissegundos
            parte_numero += 1

        print(f"Finalizado processamento de '{arquivo}'.")

if __name__ == "__main__":
    # Substitua 'input_folder' pelo caminho da pasta contendo os arquivos MP3
    pasta_entrada = "."

    # Substitua 'output_base_folder' pelo nome da pasta de saída base
    pasta_saida_base = "output_folder"

    # Substitua 1 pelo número de minutos desejado para cada trecho
    duracao_minuto = 1

    print("Iniciando o processamento dos arquivos MP3...\n")
    cortar_arquivos_mp3(pasta_entrada, pasta_saida_base, duracao_minuto)
    print("\nProcessamento concluído!")
