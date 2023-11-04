valor = []
maior = 0
menor = 0
for c in range(0,5):
    valor.append(int(input(f"Digite um numero para posição {c}: ")))
print("="*40)
print(f"Voce digitou os numeros: {valor}")

print(f"O maior numero é {max(valor)} nas posiçoes ", end='')
for c, v in enumerate(valor):
    if v == max(valor): #se o valor for o maior
        print(f"{c}...", end='')
print()
print(f"O menor numero é {min(valor)} nas posiçoes ", end='')
for c, v in enumerate(valor):
    if v == min(valor): #se o valor for o menor
        print(f"{c}...", end='')
print()