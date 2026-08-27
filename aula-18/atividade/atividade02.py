alunos = ["Arthur", "Bruno", "Caio", "Debora", "Eliza"]

print(alunos[0])
print(alunos[len(alunos)-1])
alunos[2]=input("Digite o nome do novo aluno: ")
alunos.append("Giovana")
print("---------------------------")
print("Alunos atualizado:", alunos)
print("Total de alunos:",len(alunos))
print()