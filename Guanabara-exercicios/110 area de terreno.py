def area(larg, comp):
    a = larg * comp
    print(f"A area de um terreno {larg} X {comp} é de {a}m²")


print('Controle de terrenos')
print('='*20)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
area(l,c)