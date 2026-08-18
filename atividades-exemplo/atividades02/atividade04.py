produto = input("Digite o produto: ")
preco_produto = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

total = preco_produto * quantidade

print(produto)
print("Valor total da compra: R$",total)