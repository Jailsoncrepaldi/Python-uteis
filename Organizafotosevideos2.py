import os
from datetime import datetime
import re
from shutil import move

def extrair_data_do_titulo(nome_arquivo):
    # Procurar por uma sequência de dígitos no formato diamesano no nome do arquivo
    padrao_data = re.search(r'\d{8}', nome_arquivo)
    
    if padrao_data:
        # Extrair a sequência de dígitos correspondente à data
        data_str = padrao_data.group()
        
        # Converter a string de data para um objeto datetime
        try:
            data = datetime.strptime(data_str, '%Y%m%d')
            return data
        except ValueError:
            pass
    
    return None

def obter_data_mais_recente(arquivo):
    # Obter a data de criação, se disponível
    data_criacao = datetime.fromtimestamp(os.path.getctime(arquivo))

    # Obter a data de modificação, se disponível
    data_modificacao = datetime.fromtimestamp(os.path.getmtime(arquivo))

    # Obter a data do título, se disponível
    data_titulo = extrair_data_do_titulo(os.path.basename(arquivo))

    # Escolher a data mais recente entre as disponíveis
    datas_disponiveis = [data for data in [data_criacao, data_modificacao, data_titulo] if data is not None]
    if datas_disponiveis:
        return min(datas_disponiveis)
    else:
        return None

def organizar_arquivos(origem, destino):
    # Listar todos os arquivos na pasta de origem
    arquivos = os.listdir(origem)

    for arquivo in arquivos:
        caminho_completo = os.path.join(origem, arquivo)

        # Verificar se o item é um arquivo
        if os.path.isfile(caminho_completo):
            try:
                # Obter a data mais recente entre criação, modificação e título
                data_mais_recente = obter_data_mais_recente(caminho_completo)

                if data_mais_recente:
                    # Criar caminho de destino com base na data mais recente
                    ano = str(data_mais_recente.year)
                    mes = str(data_mais_recente.month).zfill(2)
                    dia = str(data_mais_recente.day).zfill(2)

                    # Criar pastas se não existirem
                    destino_ano = os.path.join(destino, ano)
                    destino_mes = os.path.join(destino_ano, mes)
                    destino_dia = os.path.join(destino_mes, dia)

                    for pasta in [destino_ano, destino_mes, destino_dia]:
                        if not os.path.exists(pasta):
                            os.makedirs(pasta)

                    # Mover o arquivo para o destino
                    destino_arquivo = os.path.join(destino_dia, arquivo)
                    move(caminho_completo, destino_arquivo)

                    print(f'Arquivo {arquivo} movido para {destino_arquivo}')

            except Exception as e:
                print(f'Erro ao processar {arquivo}: {str(e)}')

if __name__ == "__main__":
    # Solicitar ao usuário o caminho de origem
    caminho_origem = input("Digite o caminho da pasta de origem: ").strip()

    # Substitua 'caminho_destino' pelo caminho da pasta onde deseja organizar os arquivos
    caminho_destino = 'caminho_destino'

    organizar_arquivos(caminho_origem, caminho_destino)
