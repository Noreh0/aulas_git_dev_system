print("1-Saldo")
print("2-Saque")
print("3-Depósito")
print("4-Pix")
print("5-Sair")
opcao = int(input("Digite a opção que você gostaria: "))
saldo = float(input("Digite o valor em conta: R$"))
match opcao:
    case 1:
        print("Saldo: R$", saldo)
    case 2:
        print("Saque:")
        saque = float(input("Digite o valor a ser sacado: R$"))
        if saque > saldo:
            print("Saldo indisponível")
        else:
            saldo -= saque
            print("Saldo atual igual a: R$", saldo)
            print("Saque concluído")
    case 3:
        print("Depósito")
        deposito = float(input("Digite o valor a ser depositado: R$"))
        saldo += deposito
        print("Saldo em conta: R$", saldo)
    case 4:
        print("Pix")
    case 5:
        print("Sair")
    case _:
        print("Digito inválido ou não mapeado!")