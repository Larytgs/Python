num = []
r = 'S'
while r == 'S':
    num.append(int(input("Digite um numero: ")))
    r = str(input("Quer continuar? (S/N) ")).upper()
print("="*40)
print(f"Foram digitados {len(num)} numeros")
num.sort(reverse=True)
print(f"Ordem decrescente: {num}")

if 5 in num:
    print(f"O numero 5 foi digitado na posição {num.index(5)}")
else:
    print("O numero 5 nao foi digitado na lista.")
