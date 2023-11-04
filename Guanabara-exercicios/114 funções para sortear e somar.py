from random import randint
from time import sleep
def sorteia(lista):
    print("Os numeros sorteados foram: ", end=' ')
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n}", end=' ')
        sleep(0.5)

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares de {lista} temos a soma {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)

help(sorteia)