from random import randint
maior = 0
menor = 0
numero = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))
print("Os valores sortiados sao: ")
for n in numero:
    print(f" {n} ", end='')

print(f"\nO maior numero é {max(numero)}")
print(f"O menor numero é {min(numero)}")
