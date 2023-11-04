from random import randint
from time import sleep
print("{:=^40}".format('PEDRA PAPEL TESOURA'))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input("Escolha sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("POO!!")
sleep(1)
print("-="*11)
print("Sua jogada foi {}.".format(itens[jogador]))
print("Computador jogou {}.".format(itens[computador]))
print("=-"*11)
if computador == 0: #pedra
    if jogador == 0: #pedra
        print("Deu Empate!")
    elif jogador == 1: #papel
        print("O Jogador Ganhou!")
    elif jogador == 2: #tesoura
        print("O Computador Ganhou!")
    else:
        print("Jogada Invalida!")
elif computador == 1: #papel
    if jogador == 0: #pedra
        print("Computador Ganhou!")
    elif jogador == 1: #papel
        print("Deu Empate!")
    elif jogador == 2: #tesoura
        print("Jogador Ganhou")
    else:
        print("Jogada Invalida")
elif computador == 2: #tesoura
    if jogador == 0: #pedra
        print("Jogador Ganhou!")
    elif jogador == 1: #papel
        print("Computador Ganhou!")
    elif jogador == 2: #tesoura
        print("Deu Empate!")
    else:
        print("Jogada Invalida")
