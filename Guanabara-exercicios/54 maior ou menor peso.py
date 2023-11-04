maior = 0
menor = 0
for p in range(1,6):
    peso = float(input("Peso da {} pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: #se o peso for maior q o o maior peso
            maior = peso
        if peso < menor: #se o peso for menor q o menor peso
            menor = peso
print("O maior peso lido foi de {}kg".format(maior))
print("O menor peso lido foi de {}kg".format(menor))