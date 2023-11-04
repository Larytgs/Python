import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do catetoadjacente: "))
hipotenusa = math.hypot(co, ca) # hipotenusa = (co ** 2 + ca ** 2) ** (1/2)
print("Com os comprimentos {} X {} a hipotenusa vai medir {:.3f}".format(co, ca, hipotenusa))