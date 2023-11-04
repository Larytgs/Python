print("Soma de todos os numeros impares que sao multiplos de 3, de 1 a 500")
s = 0
contador = 0
for c in range(1,501, 2):
    if c % 3 == 0:
         print (c, end=' ')
         s = s + c #s += c
         contador = contador + 1 # contador += 1
print("\nA soma de todos os {} numeros divididos por 3 é {}".format(contador, s))
print("FIM")