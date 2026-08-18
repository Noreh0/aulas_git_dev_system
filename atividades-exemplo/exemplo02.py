nome_funcionario = input("Digite o nome do Funcionário: ")
salario_funcionario = float(input("Digite o valor do salário do funcionário: "))
porcentagem_bonus = float(input("Digite o valor da porcentagem da bonificação(exemplo: 30 para 30%): "))
bonus_funcionario = salario_funcionario * (porcentagem_bonus/100)

salario_total = salario_funcionario + bonus_funcionario

print("O salário total é de R$", salario_total)