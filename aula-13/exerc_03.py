valor_sem_desconto = float(input("Digite o valor da compra: "))

if(valor_sem_desconto >= 200):
    valor_final = valor_sem_desconto - (valor_sem_desconto * 0.50)
    print("Você recebeu desconto!")
    print("A sua compra ficou de: R$ ", valor_sem_desconto)
    print("Por apenas: R$ ", valor_final)
else:
    print("Você não recebeu desconto!")
    print("Sua compra ficou em: R$ ", valor_sem_desconto)