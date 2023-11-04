salario = float(input("Qual o salario do funcionario? R$"))
if salario <= 1250:
    novo = salario + (salario * 15 / 100) #salario + 15 porcento do salario
    print("O seu aumento foi de 15%, total R${:.2f}".format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print("O seu aumento foi de 10%, total R${:.2f}".format(novo))