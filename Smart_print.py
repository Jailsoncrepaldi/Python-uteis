import os
import sys
import time
import threading
from PIL import ImageGrab, Image
from pynput import keyboard
from pystray import Icon, Menu, MenuItem

# No Windows, para evitar que o console seja exibido
if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    
    SW_HIDE = 0
    hwnd = kernel32.GetConsoleWindow()
    
    # Esconde o console apenas se não estiver em modo de depuração
    def hide_console():
        if hwnd != 0:
            user32.ShowWindow(hwnd, SW_HIDE)

# Variáveis globais
listener_active = True
listener = None  # Listener global
tray_icon = None  # Ícone da bandeja global

# Função para garantir que a pasta para salvar os screenshots exista
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Função para capturar a tela e salvar a imagem com um nome único
def capture_screen(directory):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"print_{timestamp}.jpg"
    filepath = os.path.join(directory, filename)
    screenshot = ImageGrab.grab()
    screenshot.save(filepath, "JPEG")
    print(f"Screenshot saved as {filepath}")

# Função para lidar com o evento de pressionar uma tecla
def on_press(key):
    try:
        if key == keyboard.Key.print_screen and listener_active:
            capture_screen(screenshot_directory)
    except AttributeError:
        pass

# Função para iniciar o listener do teclado
def start_listener():
    global listener
    if not listener:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        print("Listener ativado.")

# Função para parar o listener do teclado
def stop_listener():
    global listener
    if listener:
        listener.stop()
        listener = None
        print("Listener desativado.")

# Alternar o estado do listener
def toggle_listener(icon, item):
    global listener_active
    listener_active = not listener_active
    if listener_active:
        start_listener()
    else:
        stop_listener()
    item.text = "Desativar Captura" if listener_active else "Ativar Captura"

# Função para sair do programa
def exit_program(icon, item):
    print("Encerrando o programa.")
    stop_listener()
    icon.stop()
    sys.exit(0)

# Diretório onde os screenshots serão salvos
script_dir = os.path.dirname(os.path.abspath(__file__))
screenshot_directory = os.path.join(script_dir, "screenshots")
ensure_directory_exists(screenshot_directory)

# Função para criar o tray icon
def create_tray_icon():
    # Criar um ícone simples (substitua pelo seu ícone personalizado se quiser)
    icon_image = Image.new("RGB", (64, 64), color=(0, 128, 255))
    
    # Configurar o menu do tray
    menu = Menu(
        MenuItem("Desativar Captura", toggle_listener),  # Botão para ativar/desativar captura
        MenuItem("Abrir pasta de screenshots", lambda icon, item: os.startfile(screenshot_directory) if os.name == 'nt' else os.system(f'xdg-open "{screenshot_directory}"')),
        MenuItem("Sair", exit_program)  # Botão para sair
    )
    
    # Criar o ícone
    icon = Icon("ScreenCapture", icon_image, "Capturador de Tela", menu)
    return icon

def run_tray_icon():
    global tray_icon
    tray_icon = create_tray_icon()
    # Inicia o ícone da bandeja
    tray_icon.run()

if __name__ == "__main__":
    try:
        # Iniciar o listener do teclado
        print("O script será minimizado para o tray. Use o ícone para interagir.")
        start_listener()
        
        # Se estiver no Windows, esconde o console
        if os.name == 'nt':
            # Espere um pouco para garantir que a mensagem seja vista
            time.sleep(2)
            hide_console()
        
        # Executar o ícone da bandeja no thread principal
        # Isso é crucial para que o script continue rodando
        run_tray_icon()
        
    except KeyboardInterrupt:
        print("\nEncerrando o script.")
        if tray_icon:
            tray_icon.stop()
        sys.exit(0)