print("OPERADORES ARITMETICOS")
n1= int(input("Primeiro numero= "))
n2= int(input("Segundo numero= "))
#soma= n1+n2
#print("A soma é= ",soma)
#print("A soma entre", n1,"e",n2, "vale: ",soma)
#print("A soma entre {} e {} vale: {}".format(n1,n2,soma))

a = n1+n2
s = n1-n2
m = n1*n2
d = n1/n2
p = n1**n2
di = n1//n2
r = n1%n2
print("A soma é {}, a subtração é {} e a multiplicação é {}.".format(a, s, m),end=" ")
print("A divisao {:.3}, a potencia é {:.3f}".format(d,p))
print("A divisao inteira é {} e o resto da {}".format(di,r))