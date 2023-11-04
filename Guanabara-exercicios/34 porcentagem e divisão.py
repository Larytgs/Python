casa = float(input("Valor da casa: R$"))
salario = float(input("Salario do comprador: R$"))
anos = float(input("Quantos anos de financiamento? "))
minimo = salario * 30 / 100  #30 porcento de 100
prestaçao = casa / (anos * 12) #preço da casa dividido por quantos meses ele vai pagar
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa, anos))
print("A prestação sera de R${:.2f}".format(prestaçao))
if prestaçao <= minimo:
    print("Emprestimo pode se CONCEDIDO")
else:
    print("Emprestimo NEGADO")

#print("COMPARAÇÃO tem que pagar {} e o minimo é de {}".format(prestaçao, minimo))
