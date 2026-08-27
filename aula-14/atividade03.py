valor_compra = float(input("Digite o valor da compra: "))
if(valor_compra>=1000):
    desconto = valor_compra * 0.2
    valor_total = valor_compra - desconto
    print("Valor total da compra:", valor_total)
elif (valor_compra>=500):
    desconto = valor_compra * 0.1
    valor_total = valor_compra - desconto
    print("Valor total da compra:", valor_total)
else:
    print("Valor total da compra:", valor_compra, "\nSem Desconto")