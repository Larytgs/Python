print("Analisando piramides")
print("=-=-"*5)
r1 = float(input("Primeiro seguimento: "))
r2 = float(input("Segundo seguimento: "))
r3 = float(input("Terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("OS seguimentos acima PODEM FORMAR um triangulo. ", end='')
    if r1 == r2 == r3:
        print("É EQUILATERO") #todos os lados iguais
    elif r1 != r2 != r3 != r1:
        print("É ESCALENO") #todos lados diferentes
    else: #elif r1 == r2 != r3:
        print("É ISOSCELES") #dois lados iguais

else:
    print("Os seguimentos acima NÂO PODEM FORMAR triangulo.")