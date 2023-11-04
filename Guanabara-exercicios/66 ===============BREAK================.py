'''n = soma = 0
while n != 999:
    n = int(input("Digite um numero: "))
    soma += n
print("A soma vale {}".format(soma - 999)) #usando flag'''

n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
print("A soma vale {}".format(s))

