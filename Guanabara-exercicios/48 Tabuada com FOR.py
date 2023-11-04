print("Tabuada com FOR")
n = int(input("Digite um numero para ver a tabuada: "))
print("-" * 15)
for c in range(1, 11):
    print("{} X {:2} = {}".format(n, c, n*c))
print("FIM")