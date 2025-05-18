import os
import subprocess
import sys
import tempfile
import shutil

def criar_ambiente_virtual(venv_dir):
    """Cria um ambiente virtual."""
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])

def instalar_bibliotecas(venv_dir, bibliotecas):
    """Instala as bibliotecas necessárias no ambiente virtual."""
    pip_path = os.path.join(venv_dir, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')
    for biblioteca in bibliotecas:
        subprocess.check_call([pip_path, 'install', biblioteca])

def gerar_executavel(venv_dir, arquivo_python):
    """Usa o pyinstaller para gerar o executável."""
    pyinstaller_path = os.path.join(venv_dir, 'Scripts', 'pyinstaller') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pyinstaller')
    subprocess.check_call([pyinstaller_path, '--onefile', arquivo_python])

def limpar_ambiente_virtual(venv_dir):
    """Remove o ambiente virtual temporário."""
    shutil.rmtree(venv_dir)

def main():
    # Passo 1: Obter o arquivo Python
    arquivo_python = input("Digite o caminho do arquivo Python: ")

    # Passo 2: Obter as bibliotecas necessárias
    bibliotecas = input("Digite as bibliotecas necessárias (separadas por vírgulas, ou pressione Enter se usar apenas bibliotecas padrão): ").split(',')
    bibliotecas = [b.strip() for b in bibliotecas if b.strip()]  # Limpar espaços extras e remover entradas vazias

    # Passo 3: Criar um ambiente virtual temporário
    venv_dir = tempfile.mkdtemp()  # Cria um diretório temporário
    print(f"Criando ambiente virtual em {venv_dir}...")

    try:
        # Passo 4: Criar ambiente virtual
        criar_ambiente_virtual(venv_dir)

        # Passo 5: Instalar bibliotecas (somente se especificadas)
        if bibliotecas:
            print(f"Instalando as bibliotecas: {', '.join(bibliotecas)}")
            instalar_bibliotecas(venv_dir, bibliotecas)
        else:
            print("Nenhuma biblioteca especificada. Usando apenas bibliotecas padrão.")

        # Passo 6: Instalar pyinstaller no ambiente virtual
        print("Instalando pyinstaller...")
        instalar_bibliotecas(venv_dir, ['pyinstaller'])

        # Passo 7: Gerar o executável
        print(f"Gerando o executável para {arquivo_python}...")
        gerar_executavel(venv_dir, arquivo_python)
        print("Executável gerado com sucesso!")

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        # Passo 8: Limpar o ambiente virtual temporário
        print("Limpando o ambiente virtual...")
        limpar_ambiente_virtual(venv_dir)
        print("Ambiente virtual removido.")

if __name__ == "__main__":
    main()
