saldo = 5879.23

valor_saque = float(input("Informe o valor do saque desejado: R$"))

if(valor_saque <= saldo):
    print("Saque autorizado com sucesso!")
    print("Seu saldo atual é de: R$", (saldo - valor_saque))
else:
    print("Saldo insuficiente")
    print("Seu saldo atual é de: R$", saldo)