import keyboard

def on_press(event):
    print(f"{event.name} pressionado")

def on_release(event):
    print(f"{event.name} liberado")

keyboard.on_press(on_press)
keyboard.on_release(on_release)

input("Pressione qualquer tecla para sair\n")
