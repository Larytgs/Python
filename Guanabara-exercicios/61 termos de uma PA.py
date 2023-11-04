print("="*20)
print("10 TERMOS DE UMA PA(progressao aritmetica")
print("="*20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao do PA: "))
termo = primeiro
cont = 1
while cont <= 10: #ate chegar no 10
    print("{}".format(termo), end=' -> ') #vai começar com o termo, q é o primeiro numero
    termo = termo + razao
    cont += 1
print("ACABOU")
