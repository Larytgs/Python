from random import randint
palpites = 0
computador = randint(0, 10)
print("Sou seu computador...")
print("Acabei de pensar em um numero entre 0 a 10.")
print("Sera que voce consegue adivinhar qual foi? ")
acertou = False #pq vc ainda n acertou
while not acertou:
    jogador = int(input("Qual é o seu papite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais..tente mais uma vez. ")
        elif jogador > computador:
            print("Menos.. tente mais uma vez.")

print("Acertou. Acertou com {} tentativas. Parabéns!".format(palpites))