"""
| -------------
| Temp Cleaner
| -------------
| Algoritmo que limpa os diretórios temp e %temp% do Windows.
| -------------
| [Tutorial]
| -------------
| Por padrão esse sistema vai limpar apenas as pastas temp e %temp% do seu computador. Para que isso funcione
| você deve navegar até o caminho Functions/directories.py e lá mudar no nome do seu usuário, por padrão vai estar
| "anton".
| Depois disso você pode executar o main (este arquivo daqui).
| Caso queria adicionar um novo caminho para ser limpo também você pode ou adicionar no array de diretórios
| no caminho que já foi explicado acima, ou usar um procedimento chamado "add_directory()" passando como parâmetro
| o caminho da pasta que vai ser limpa também (lembrando que se houver uma barra invertida você deve inserir
| mais uma ao lado). Isso deve ser feito antes do método "main()" ser executado!
"""
from Functions.functions import clean_directory, log, add_directory
from Functions.directories import directories_path as directories


def main():
    clean_directory(directories)
    log()


# add_directory("C:\\Exemplo\\De\\Caminho")

main()
