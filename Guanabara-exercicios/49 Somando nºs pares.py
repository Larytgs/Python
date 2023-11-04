print("Somando os numeros pares")
s = 0
cont= 0
for c in range(1, 7):
    n = int(input("Digite um numero: "))
    if n % 2 == 0: #se o numero for par(dividido por 2) e verificar sea divisçao é igual a zero
       s = s + n
       cont = cont + 1
print("Voce informou {} numeros PARES. A soma dos numeros é {}".format(cont, s))
print("FIM")
