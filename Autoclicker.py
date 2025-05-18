import time
import threading
import keyboard
import pyautogui

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.click_thread = None
        self.delay = 0.05  # Altere o atraso conforme necessário

    def click(self):
        while self.clicking:
            pyautogui.click()
            time.sleep(self.delay)

    def start_clicking(self):
        if not self.clicking:
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click)
            self.click_thread.start()

    def stop_clicking(self):
        self.clicking = False
        if self.click_thread:
            self.click_thread.join()

auto_clicker = AutoClicker()

def toggle_auto_clicker():
    if auto_clicker.clicking:
        auto_clicker.stop_clicking()
        print("Clique automático parado")
    else:
        auto_clicker.start_clicking()
        print("Clique automático iniciado")

keyboard.add_hotkey('space', toggle_auto_clicker)

print("Pressione a barra de espaço para iniciar/parar o clique automático")
keyboard.wait('esc')  # Espera até que a tecla 'esc' seja pressionada antes de encerrar o programa
