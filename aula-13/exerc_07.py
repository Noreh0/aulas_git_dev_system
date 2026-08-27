verificar_idade = int(input("Digite a sua idade: "))
verificar_autorizacao = False

if(verificar_idade >= 16 or verificar_autorizacao==True):
    print("Acesso Permitido!")
else:
    print("Acesso Negado!")