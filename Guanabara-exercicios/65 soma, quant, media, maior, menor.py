num = 0
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss': #enquanto a resposta por sim
    num = int(input("Digite um numero: "))
    soma = soma + num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
media = soma / quant
print("Voce digitou {} numeros e a media foi {}".format(quant, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
