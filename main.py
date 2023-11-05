"""
| -------------
| Temp Cleaner
| -------------
| Algoritmo que limpa os diretórios temp e %temp% do Windows.
"""
from Functions.functions import clean_directory, log
from Functions.directories import directories_path as directories


def main():
    clean_directory(directories)
    log()


main()
