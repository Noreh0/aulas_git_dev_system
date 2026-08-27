calcular_notas = True
media = 0
contador = 0

while calcular_notas:
    print("1 - adicionar notas")
    print("2 - sair")
    opcao = int(input("digite uma opção entre 1 e 2: "))
    if opcao == 1:
        nota = float(input("Digite a nota do aluno: "))
        media = media + nota
        contador = contador + 1
    elif opcao == 2:
        print("Saindo, até mais!")
        print("Total de alunos:", contador)
        print("Média da turma:", media/contador)
        calcular_notas = False
    else:
        print("Digito inválido!")