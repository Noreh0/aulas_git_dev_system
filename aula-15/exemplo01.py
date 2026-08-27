codigo = int(input("digite o codigo: "))

match codigo:
    case 200:
        print("Sucesso")
    case 300:
        print("Erro")
    case _:
        print("Código não esta dentro das especificações!")
