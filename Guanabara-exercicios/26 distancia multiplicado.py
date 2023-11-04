distancia = float(input("Qual é a distancia da sua viagem? "))
print("Voce esta prestes a começar uma viagem de {}km.".format(distancia))
if distancia <= 200:
    print("E o preço da sua passagem sera de R${:.2f}".format(distancia * 0.50))
else:
    print("E o preço da sua passagem sera de R${:.2f}".format(distancia * 0.45))