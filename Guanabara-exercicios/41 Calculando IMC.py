print("CALCULANDO IMC")
peso = float(input("Qual é o seu peso? (kG) "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura ** 2) #peso dividido pela altura ao quadrado
print("O IMC dessa pessoa é de {:.1f}.".format(imc))
if imc < 18.5:
    print("Esta Abaixo do Peso normal")
elif 18.5 <= imc < 25: #imc >= 18.5 and imc < 25: Entre um e o outro
    print("Esta com o Peso Ideal")
elif 25 <= imc < 30:
    print("Esta Sobrepeso")
elif 30 <= imc < 40:
    print("Esta com Obesidade")
else:
    print("Esta com Obesidade Mórbida")