a = int(input("Digite primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

'''if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
    e fazer com maior tbm'''

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
