real = float (input("Quanto dinheiro tem na sua carteira? R$"))
dolar = real / 4.73
print("Com R${:.2f} voce pode comprar US${:.2f}".format(real, dolar))