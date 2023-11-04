print("="*20)
print("10 TERMOS DE UMA PA(progressao aritmetica")
print("="*20)
termo = int(input("Primeiro termo: ")) #começa c um nº
razao = int(input("Razão: ")) #pulando de ...
decimo = termo + (10 - 1) * razao #calcular o decimo termo
for c in range(termo, decimo + razao, razao):
    print("{}".format(c), end=' -> ')
print("ACABOU")