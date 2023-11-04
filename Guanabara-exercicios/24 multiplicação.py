carro = int(input("Qual foi o seu limite de velocida? "))
if carro > 80:
    print("A multa vai custar R$7,00 por cada km acima do limite.")
    multa = (carro - 80) * 7
    print("Total da multa: {}R$".format(multa))
else:
    print("Parabens, voce esta no limite de velocidade")