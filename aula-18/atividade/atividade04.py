lista_compras: list[str] = []

produto1 = input("Digite o primeiro produto da lista de compras: ")
produto2 = input("Digite o segundo produto da lista de compras: ")
produto3 = input("Digite o terceiro produto da lista de compras: ")
lista_compras.append(produto1)
lista_compras.append(produto2)
lista_compras.append(produto3)

print("\n========Lista de Compras========")
print("Todos os produtos:", lista_compras)
print("Total de produtos:", len(lista_compras))
print("Primeiro produto:",lista_compras[0])
print("Último produto:",lista_compras[len(lista_compras)-1])