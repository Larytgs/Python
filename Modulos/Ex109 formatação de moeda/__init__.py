import moeda

p = float(input("Digite um preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}') #o 'True' é a formatação nova
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O aumento de 30% vale {moeda.aumentar(p, 30, True)}')
print(f'O deconto de 10% vale {moeda.diminuir(p, 10, True)}')
