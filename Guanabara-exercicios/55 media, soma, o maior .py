soma = 0
idade = 0
media = 0
maioridadehomem = 0
nomedovelho = 0
totmulher20 = 0
for p in range(1,5):
    print("---- {}º PESSOA ----".format(p))
    nome = str(input("Digite seu nome: ")).strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("F/M? ")).strip()
    soma = soma + idade
    if p == 1 and sexo in 'Mm': #se for a 1º pessoa e for masculino
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: #se ainda é masculino e a idade dele é o maior
        maioridadehomem = idade
        nomedovelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = soma / 4 #dividido por 4 pessoas
print("A media de idade do grupo é de {} anos".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomedovelho))
print("Ao todo são {} mulherer com menos de 20 anos.".format(totmulher20))