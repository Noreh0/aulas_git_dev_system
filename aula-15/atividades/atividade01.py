opcao = int(input("Digite a opção que você gostaria(1-3):"))
match opcao:
    case 1:
        print("cadastro")
    case 2:
        print("consulta")
    case 3:
        print("sair")
    case _:
        print("sair")
print("programa encerrado!")