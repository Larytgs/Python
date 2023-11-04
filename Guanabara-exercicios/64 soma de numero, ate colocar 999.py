soma = 0
cont = 0
num = 0
num = int(input("Digite um numero [999 para parar]: "))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input("Digite um numero [999 para parar]: "))
print("Voce digitou {} numeros e a soma entre eles foi {}".format(cont, soma))

#colocando na frase antes, ele desconsidera depois, mas pode fazer :
#print("Voce digitou {} numeros e a soma entre eles foi {}".format(cont - 1, soma - 999))
