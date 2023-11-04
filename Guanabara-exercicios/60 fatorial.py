'''from math import factorial
num = int(input("Digite um numero para ver o seu fatorial: "))
f = factorial(num)
print("Calculando  {}! = {}".format(num, f))'''
num = int(input("Digite um numero para ver o seu fatorial: "))
c = num #começa com o numero q digitou
f = 1 #tem q começar com 1 no fatorial ou multiplicação
print("Calculando {}! = ".format(num), end='')
while c > 0:
    print("{}".format(c), end='') #pra n pular de linha
    print(" X " if c > 1 else " = ", end='') #se tiver um nº coloque x, se nao =
    f = f * c
    c -= 1 #pra mostrar a sequencia dos numeros decrescente
print("{}".format(f))
