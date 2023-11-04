'''for c in range(1, 11):
    print(c,end=' ')
print("FIM")'''

'''c = 1
while c < 11:
    print(c, end=' ')
    c = c + 1
print("FIM")'''

r = 'S'
while r == 'S':
    n = int(input("Digite um numero: "))
    r = str(input("Gostaria de continuar? (S/N) ")).upper()
print("FIM")

'''print("Quantos IMPARES e Quantos PARES")
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0: #se digitar o 0, n vai contar como par, e sim o resto
        if n % 2 == 0: #se o resto da divisao for igual a 0
            par += 1 # par = par + 1
        else:
            impar += 1
print("Voce dijitou {} numeros pares e tantos {} impares".format(par, impar))'''