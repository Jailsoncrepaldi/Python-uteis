import os

def delete_empty_folders(root_dir):
    deleted_folders = []

    for root, dirs, files in os.walk(root_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)

            if not os.listdir(dir_path):
             try:
                 os.rmdir(dir_path)
                 deleted_folders.append(dir_path)
             except:
                pass
    with open('deleted_folders.txt', 'w') as file:
        file.write('\n'.join(deleted_folders))

root_dir = input("Digite o caminho da pasta que deseja vasculhar: ")
delete_empty_folders(root_dir)
