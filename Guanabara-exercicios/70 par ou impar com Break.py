from random import randint
print("{:=^40}".format(' PAR ou IMPAR '))
v = 0
while True:
    jogador = int(input("Digite um numero: "))
    computador = randint(0, 10) #vai escolher de 0 a 10
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input("Voce escolhe Par ou Impar? [P/I] ").upper()[0].strip())
    print(f"Voce escolheu {jogador} e o computador {computador} e o Total de {total}")
    print("DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if tipo == 'P':
        if total % 2 == 0:
            print("Voce venceu!")
            v += 1
        else:
            print("Voce perdeu!")
            break
    if tipo == 'I':
        if total % 2 == 1:
            print("Voce venceu!")
            v += 1
        else:
            print("Voce perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Voce venceu {v} vezes")