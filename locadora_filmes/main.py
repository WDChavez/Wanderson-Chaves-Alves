from filmes import (
    adicionar_filme,
    editar_filme,
    listar_filmes,
    buscar_filme,
    alugar_filme,
    devolver_filme
)

from dados import lista

def menu(lista):
    while True:
        print("\n=====Menu=====")
        print("1- Adicionar filme")
        print("2- Editar filme")
        print("3- Listar filmes")
        print("4- Buscar filme por titulo")
        print("5- Alugar filme")
        print("6- Devolver filme")
        print("7- Sair\n")
    
        op = input("Escolha uma opção: ")

        if op == "1":
            adicionar_filme(lista)
    
        elif op == "2":
            editar_filme(lista)

        elif op == "3":
            listar_filmes(lista)

        elif op == "4":
            buscar_filme(lista)

        elif op == "5":
            alugar_filme(lista)

        elif op == "6":
            devolver_filme(lista)

        elif op == "7":
            print("Saindo!")
            break

    else:
        print("Opção inválida!")
    
    
if __name__ == "__main__":
    print("Entrou no main")
    menu(lista)