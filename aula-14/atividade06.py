peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura ** altura)
print("Seu IMC é:", IMC)

if IMC >= 30:
    print("Obesidade.")
elif IMC >= 25:
    print("Sobrepeso.")
elif IMC >= 18.5:
    print("Peso Ideal.")
else:
    print("Abaixo do peso.")