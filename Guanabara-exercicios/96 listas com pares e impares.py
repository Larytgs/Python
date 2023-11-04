num = [[], []] #duas listas em um só
valor = 0
print(f'\033[34m{"Digite 7 numeros, para ver os pares e impares.":=^60}\033[m')
for n in range(1, 8):
    valor = int(input(f"Digite o {n}º valor: "))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print("="*40)
num[0].sort()
num[1].sort()
print(f"Os valores pares digitados foram: {num[0]}") #a primeira lista
print(f"Os valores impares digitados foram : {num[1]}") #a segunda lista