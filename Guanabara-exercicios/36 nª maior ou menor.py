n1 = int((input("Digite um numero: ")))
n2 = int(input("Digite o segundo numero: "))

if n1 > n2:
    print("O numero {} é o maior.".format(n1))

elif n2 > n1:
    print("O numero {} é o maior.".format(n2))

else:
    print("Os dois numeros sao iguais.")
