nome_funcionario = input("Digite o nome do funcionario: ")
salario_funcionario = float(input("Digite o salario do funcionario: "))
hora_extra = float(input("Digite o total da hora extra ganha: "))
valor_desconto = float(input("Valor total do desconto: "))

salario_total = (salario_funcionario + hora_extra) - valor_desconto

print("O funcionario:", nome_funcionario, "tem a receber R$", salario_total)