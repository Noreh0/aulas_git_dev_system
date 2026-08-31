cidades = []

for cidade in range(5):
    nome_cidade = input("Digite o nome da cidade: ")
    cidades.append(nome_cidade)

for i in range(len(cidades)):
    print(i+1, cidades[i])