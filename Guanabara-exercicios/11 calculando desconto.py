valor = float(input("Qual é o preço do produto? R$"))
desconto = valor - (valor * 5 / 100)
print("O desconto do produto de {} é de {}".format(valor, desconto))