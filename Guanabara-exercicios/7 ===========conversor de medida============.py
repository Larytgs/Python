m = float(input("Digite uma distancia em metros: "))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
#km hectometro decametro m decimetro cm mm
print("A medida em {} metros corresponde a:\n{}km\n{}hm\n{}dam".format(m, km, hm, dam))
print("{}dm\n{:.0f}cm\n{:.0f}mm".format(dm, cm, mm))