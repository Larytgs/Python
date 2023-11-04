valores = [] # ou valores = list()
'''valores.append(8)
valores.append(10)
valores.append(2)'''

for v in valores: #p cada valor em valores
    print(f"{v}...", end='')

#for c, v in enumerate(valores): #enumerate, ele pega tanto a chave tanto o valor
#    print(f"\nNa posição {c} encontrei o valor {v}!", end='')

for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores): #enumerate, ele pega tanto a chave tanto o valor
    print(f"\nNa posição {c} encontrei o valor {v}!", end='')