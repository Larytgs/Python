temporario = list()
principal = list()
maior = menor = 0
while True:
    temporario.append(str(input("Qual o seu nome? ")))
    temporario.append(float(input("Qual o seu peso? Kg")))
    if len(principal) == 0: #sen cadastrei ninguem ainda, n tem nd na lista
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:]) #o temporario vai jogarp o princial
    temporario.clear() #depois tem q excluir o temporario,para n ficar repetido
    r = str(input("Quer continuas? (S/N) ")).upper().strip()
    print("="*20)
    if r in 'Nn':
        break
print(f"Ao todo, voce cadastrou {len(principal)} pessoas.")
print(f"O maior peso foi {maior}. Peso de ", end=' ')
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}", end=' ')
print()
print(f"O menor peso foi {menor}. Peso de ", end=' ')
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}", end=' ')
