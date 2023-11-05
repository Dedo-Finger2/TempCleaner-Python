"""
| -------------
| Temp Cleaner
| -------------
| Algoritmo que limpa os diretórios temp e %temp% do Windows.
"""
# Importando bibliotecas
import os
from os.path import isfile, isdir
import shutil
from datetime import date

# Arquivos que não puderam ser deletados
system_del_status = {
    'folders': 0,
    'files': 0,
    'remain': 0,
}

directories = [
    "C:\\Windows\\Temp",
    "C:\\Users\\anton\\AppData\\Local\\Temp",
]

deleted_files = []
deleted_folders = []
remain_items = []


def clean_directory(directories_list: list, status: dict):
    for directory in directories_list:
        directory_items = get_all_items(directory)
        for file_folder in directory_items:
            # Tentar deletar o item, se não der, pular a interação
            try:
                # Se for um arquivo, deletar com os
                if isfile(directory + "\\" + file_folder):
                    os.remove(directory + "\\" + file_folder)
                    status['files'] += 1
                    deleted_files.append(file_folder)
                # Se for uma pasta, deletar com shutil
                else:
                    shutil.rmtree(directory + "\\" + file_folder)
                    status['folders'] += 1
                    deleted_folders.append(file_folder)
            except Exception as e:
                print(e)
                status['remain'] += 1
                remain_items.append(file_folder)
    show_output(status)


def get_files(directory: str):
    for file in get_all_items(directory):
        if isfile(file):
            yield directory + "\\" + file
        else:
            continue


def get_folders(directory: str):
    for folder in get_all_items(directory):
        if isdir(folder):
            yield directory + "\\" + folder
        else:
            continue


def show_output(status: dict):
    print("\n| ---------------------------------------")
    print("| Finished--")
    print("| ---------------------------------------")
    print(f"| Arquivos deletados: {status['files']}\n"
          f"| Pastas deletadas: {status['folders']}\n"
          f"| Item que não foram deletados: {status['remain']}")
    print("| ---------------------------------------")


def get_all_items(directory: str):
    all_items = os.listdir(directory)
    return all_items


def add_directory(directory_list: list, path: str):
    directory_list.append(path)


def log(status: dict):
    today = date.today().strftime('%Y-%m-%d')
    if isfile(f"Log/log - {today}.txt"):
        with open(f"Log/log - {today}.txt", 'a') as log_file:
            log_file.write("\n\n---------------------------[INICIO]---------------------------")

            log_file.write(f"\n| Arquivos deletados: [ {status['files']} ]\n")
            for file in deleted_files:
                log_file.write(f"\t- {file}\n")

            log_file.write(f"| Pastas deletadas: [ {status['folders']} ]\n")
            for folder in deleted_folders:
                log_file.write(f"\t- {folder}\n")

            log_file.write(f"| Items que sobraram: [ {status['remain']} ]\n")
            for item in remain_items:
                log_file.write(f"\t- {item}\n")
            log_file.write("---------------------------[FIM]---------------------------")
    else:
        with open(f'Log/log - {today}.txt', 'w') as log_file:
            log_file.write("\n\n---------------------------[INICIO]---------------------------")

            log_file.write(f"\n| Arquivos deletados: [ {status['files']} ]\n")
            for file in deleted_files:
                log_file.write(f"\t- {file}\n")

            log_file.write(f"\n| Pastas deletadas: [ {status['folders']} ]\n")
            for folder in deleted_folders:
                log_file.write(f"\t- {folder}\n")

            log_file.write(f"\n| Items que sobraram: [ {status['remain']} ]\n")
            for item in remain_items:
                log_file.write(f"\t- {item}\n")
            log_file.write("---------------------------[FIM]---------------------------")


def main():
    clean_directory(directories, system_del_status)
    log(system_del_status)


main()
