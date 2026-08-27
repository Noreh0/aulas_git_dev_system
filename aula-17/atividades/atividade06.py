alunos = int(input("Digite a quantidade de alunos: "))
total = 0

for i in range(alunos):
    nota = float(input("Digite a nota do aluno: "))
    total += nota
    
print("Média da nota da turma é: ", total/alunos)