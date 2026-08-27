nomes: list[str] = []

for i in range (5):
    nome = input( "Digite o nome: " )
    print(i+1,"-", nome)
    nomes.append(nome)
