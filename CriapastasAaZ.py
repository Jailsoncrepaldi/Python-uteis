import os

def create_folders():
    for i in range(10):
        folder_name = str(i)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Pasta {folder_name} criada com sucesso!")

    for letter in range(65, 91):
        folder_name = chr(letter)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Pasta {folder_name} criada com sucesso!")

create_folders()
