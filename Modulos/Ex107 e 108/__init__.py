import moeda

p = float(input("Digite um preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O aumento de 30% vale {moeda.moeda(moeda.aumentar(p, 30))}')
print(f'O deconto de 10% vale {moeda.moeda(moeda.diminuir(p, 10))}')

