from datetime import date  #tem q importar para funcionar
print("ALISTAMENTO DO SERVIÇO MILITAR") #feito em 2023, entao quem nasceu em 2005 tem 18 anos
atual = date.today().year #qual é o ano de hoje?
nasc = int(input("Qual o seu ano de nascimento? "))
idade = atual - nasc #para saber a idade
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))

if idade == 18:
    print("Esta na hora de se alistar imediatamente!")
elif idade < 18:
    saldo = 18 - idade
    print("Voce tem que se alistar no serviço militar, falta {} anos.".format(saldo))
    ano = atual + saldo #em que ano vai ser o alistamento
    print("Seu alistamento sera em {}".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Ja passou do tempo de se alistar ha {} anos.".format(saldo))
    ano = atual - saldo #em que ano foi o alistamento
    print("Seu alistamento foi em {}".format(ano))
