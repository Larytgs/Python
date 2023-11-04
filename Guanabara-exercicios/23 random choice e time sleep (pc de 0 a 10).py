import time
from random import choice
print("-=-" * 15)
print("Vou pensar em numero de 0 a 10")
print("-=-" * 15)
num = int(input("Em que numero eu pensei? "))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = choice(lista)
print("PROCESSANDO.....")
time.sleep(3)
if escolhido != num:
    print("GANHEI, Eu pensei no numero {} e não no {}".format(escolhido, num))
else:
    print("PARABENS. Voce conseguiu acertar!")