def adicionar_filme(lista):

    filme = {
    "titulo": input("Digite o nome do filme: "),
    "diretor": input("DIgite o nome do direto: "),
    "ano": int(input("Digite o ano de lançamento: ")),
    "status": ("Disponível"),
    "prazo": 0
    }

    lista.append(filme)
    print("Filme adicionado com sucesso!")

def editar_filme(lista):

    titulo = input("Qual filme deseja editar? ")

    for filme in lista:

        if filme["titulo"] == titulo:

            filme["titulo"] = input("Qual o titulo: ")
            filme["diretor"] = input("Qual o nome do direto? ")
            filme["ano"] = int(input("Qual ano de lançamento? "))
            print("Filme atualizado!")
            print(f"Título: {filme['titulo']} - Diretor: {filme['diretor']} - Ano: {filme['ano']}")
            return

    print("Filme não encontrado!")

def listar_filmes(lista):

    print("\n------Lista de Filmes-------")

    for filme in lista: 
        print(f"Título: {filme['titulo']}")
        print(f"Diretor: {filme['diretor']}")
        print(f"Ano: {filme['ano']}")
        print(f"Status: {filme['status']}")
        print("---------------------")

def buscar_filme(lista):
    titulo = (input("Qual filme você procura? "))

    for filme in lista: 
        if filme['titulo'] == titulo:
            print(f"Filme: {filme['titulo']}")
            print(f"Diretor: {filme['diretor']}")
            print(f"Ano: {filme['ano']}")
        print(f"Status: {filme['status']}")
        return

    print("Filme não encontrado!")

def alugar_filme(lista):

    titulo = input("Qual filme deseja alugar? ")

    for filme in lista:
        if filme["titulo"] == titulo:

            if filme["status"] == "Alugado":
                print("Filme já está alugado!")
                return

            dias = int(input("Quantos dias de aluguel? "))

            filme["status"] = "Alugado"
            filme["prazo"] = dias

            print("Filme alugado com sucesso!")
            print(f"Prazo de devolução: {dias} dias")
            return

    print("Filme não encontrado!")

def devolver_filme(lista):

    titulo = input("Qual filme deseja devolver? ")

    for filme in lista:
        if filme["titulo"] == titulo:

            if filme["status"] == "Disponível":
                print("Este filme já está disponível!")
                return

            filme["status"] = "Disponível"
            filme["prazo"] = 0

            print("Filme devolvido com sucesso!")
            return

    print("Filme não encontrado!")