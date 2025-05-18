import os

def rename_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"A pasta {folder_path} não existe.")
        return

    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)

    if file_count == 1:
        print("A pasta tem apenas um arquivo, o nome não será alterado.")
        return

    folder_name, extension = os.path.splitext(os.path.basename(folder_path))
    new_folder_name = f"{folder_name}({file_count}){extension}"
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)

    os.rename(folder_path, new_folder_path)
    print(f"Pasta renomeada para {new_folder_name}.")

folder_path = input("Informe o caminho da pasta a ser renomeada: ")
lista=os.listdir(folder_path)
for item in lista:
    print(item)
    rename_folder(folder_path+"/"+item)
