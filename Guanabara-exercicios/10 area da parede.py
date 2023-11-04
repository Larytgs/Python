larg = float(input("Quantos metros de largura tem a parede? "))
alt = float(input("E quantos de altura? "))
area = larg * alt
print("Sua parede tem a dimensao de {}X{} e a sua area é de {}m".format(larg, alt, area))
tinta = area / 2
print("Para pintar essa parede voce vai precisar de {} de tinta.".format(tinta))