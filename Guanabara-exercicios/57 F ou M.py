sexo = 0
sexo = str(input("Qual o seu sexo?[F/M] ")).upper().strip()
while sexo not in 'Ff/Mm':
    sexo = str(input("Dados INVALIDO, digite novamente: ")).upper().strip()
print("Sexo {}, registrado com sucesso".format(sexo))

#QUERO Q MOSTRE A PALAVRA FEMININO/MASCULINO
'''sexo = 0
sexof = 'Feminino'
sexom = 'Masculino'
sexo = str(input("Qual o seu sexo?[F/M] ")).upper().strip()
while sexo not in 'Ff/Mm':
    sexo = str(input("Dados INVALIDO, digite novamente: ")).upper().strip()
    if sexo == 'Ff':
        print("Sexo {}, registrado com sucesso.".format(sexof))
    elif sexom == 'Mm':
        print("Sexo {}, registrado com sucesso.".format(sexom))
print("Sexo {}, registrado com sucesso.".format(sexo)'''

