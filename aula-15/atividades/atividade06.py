print("1-centimetros")
print("2-quilometros")
print("3-milimetros")

opcao = int(input("Digite uma das opções acima para converter a metragem: "))
valor_metros = float(input("Digite o valor em metros: "))

match opcao:
    case 1:
        valor_cent = valor_metros * 100
        print("A sua converção para centimetros ficou:", valor_cent)
    case 2:
        valor_km = valor_metros / 1000
        print("A sua converção para Quilometros ficou:", valor_km)
    case 3:
        valor_mili = valor_metros * 1000
        print("A sua converção para Milimetros ficou:", valor_mili)
    case _:
        print("Opção inválida!")