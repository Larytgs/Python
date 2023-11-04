numeros = list()
r = 'S'
while r == 'S':
    n = int(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Nao vou adicionar...")
    r = str(input("Quer continuar? (S/N) ")).upper()
print()
print("="*30)
numeros.sort()
print(f"Voce digitou os valores {numeros} na ordem crescente.", end='')

#Ou fazer assim:
'''numeros = []
while True:
    n = int(input("Digite um numero: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Nao vou adicionar...")
    r = str(input("Quer continuar? (S/N) ")).upper()
    if r in 'Nn':
        break
print()
print("="*30)
numeros.sort()
print(f"Voce digitou os valores {numeros} na ordem crescente.", end='')'''