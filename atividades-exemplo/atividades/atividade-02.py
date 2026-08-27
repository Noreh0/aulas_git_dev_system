idade_usuario = int(input("Digite a sua idade: "))
altura_usuario = float(input("Digite a sua altura(M): "))
peso_usuario = float(input("Digite seu peso(Kg): "))

imc = peso_usuario / (altura_usuario * altura_usuario)

print("Idade:", idade_usuario)
print("Seu Imc é:", imc, "\n")

print("| IMC            | Classificação      |")
print("| -------------- | ------------------ |")
print("| Menor que 18,5 | Abaixo do peso     |")
print("| 18,5 a 24,9    | Peso normal        |")
print("| 25 a 29,9      | Sobrepeso          |")
print("| 30 a 34,9      | Obesidade grau I   |")
print("| 35 a 39,9      | Obesidade grau II  |")
print("| 40 ou mais     | Obesidade grau III |")