import os
import shutil
from os.path import isfile, isdir

folders_deleted: int = 0
file_deleted: int = 0
items_not_deleted: int = 0

# Pegar o diretório temp
temp_path: str = "C:\\Windows\\Temp"

# Pegar diretório %temp%
percent_temp_path: str = "C:\\Users\\anton\\AppData\\Local\\Temp"

# Listar itens dentro da temp
temp_items: list = os.listdir(temp_path)

# Listar itens dentro da %temp%
percent_temp_items: list = os.listdir(percent_temp_path)

# Para cada item dentro da temp
for item in temp_items:
    # Tentar deletar o item, se não der, pular a interação
    try:
        # Se for um arquivo, deletar com os
        if isfile(temp_path + "\\" + item):
            os.remove(temp_path + "\\" + item)
            file_deleted += 1
        # Se for uma pasta, deletar com shutil
        else:
            shutil.rmtree(temp_path + "\\" + item)
            folders_deleted += 1
    except Exception as e:
        print(e)
        items_not_deleted += 1

# Para cada item dentro da %temp%
for item in percent_temp_items:
    # Tentar deletar o item, se não der, pular a interação
    try:
        # Se for um arquivo, deletar com os
        if isfile(percent_temp_path + "\\" + item):
            os.remove(percent_temp_path + "\\" + item)
            file_deleted += 1
        # Se for uma pasta, deletar com shutil
        else:
            shutil.rmtree(percent_temp_path + "\\" + item)
            folders_deleted += 1
    except Exception as e:
        print(e)
        items_not_deleted += 1

print("\n| ---------------------------------------")
print("| Finished--")
print("| ---------------------------------------")
print(f"| Arquivos deletados: {file_deleted}\n"
      f"| Pastas deletadas: {folders_deleted}\n"
      f"| Item que não foram deletados: {items_not_deleted}")
print("| ---------------------------------------")
