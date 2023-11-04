print("="*20)
print("10 TERMOS DE UMA PA(progressao aritmetica")
print("="*20)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao do PA: "))
termo = primeiro
cont = 1
totaldetermos = 0
maistermos = 10 #começa com 10 termos
while maistermos != 0:
    totaldetermos = totaldetermos + maistermos
    while cont <= totaldetermos:
        print("{}".format(termo), end=' -> ') #vai começar com o termo, q é o primeiro numero
        termo += razao
        cont += 1
    print("PAUSA")
    maistermos = int(input("Quantos termos voce quer mostrar mais? "))
print("Progressao finalisada com {} termos mostrados.".format(totaldetermos))