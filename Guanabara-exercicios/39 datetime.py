from datetime import date
atual = date.today().year
print("Confederação Nacional de Natação" )
nasc = int(input("Ano de nascimento: "))
idade= atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
print("O atleta tem {} anos.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SENIOR")
else:
    print("Classificação: MASTER")