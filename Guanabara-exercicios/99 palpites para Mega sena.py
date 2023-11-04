from random import randint
from time import sleep
lista = []
jogos = list()
print('='*40)
print("=" * 10, "\033[1;34mJOGO NA MEGA SENA\033[m", "=" * 10)
print('='*40)
quant = int(input("\033[37mQuantos jogos voce quer que eu sorteie? \033[m"))
tot = 1 #total de vezes q ele vai sortear
while tot <= quant: #enquanto o total for <= a quantidade de jogos
    cont = 0
    while True:
        num = randint(1, 25) #vai sortear nºs de 1 a 60
        if num not in lista: # se o nº n estiver na lista
            lista.append(num) #vc adiciona ele
            cont += 1
        if cont >= 6: #se ja sorteou 6 numeros, vai parar
            break
    lista.sort()
    jogos.append(lista[:]) #vai criar uma copia da lista
    lista.clear() #e vai excluir a lista
    tot += 1 #para n entrar em loop
print(f"\033[34m{f'SORTEANDO {quant} JOGOS':=^40}\033[m")
for i, l in enumerate(jogos): #para cada indice com a lista dos jogos
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print("=" * 9, "\033[1;4;36m< BOA SORTE! >\033[m", "=" * 9)
