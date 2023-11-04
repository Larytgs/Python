n1 = float(input("Primeiranota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
m = (n1 + n2) / 2
print("A media do aluno é {:.1f}".format(m))
if m >= 7:
    print("O aluno PASSOU na prova! APROVADO")
elif m >= 5 and m < 7: # 7 > m >=5:
    print("O aluno NÂO passou na prova! RECUPERAÇÂO")
elif m < 5:
    print("O aluno esta REPROVADO!")
