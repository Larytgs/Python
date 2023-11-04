print("Numero PRiMO") #só é divisivel por 1 e ele mesmo
num = int(input("Digite um numero: "))
tot = 0 #o numero de divisiveis
for c in range(1, num + 1):
    if num % c == 0: #se o numero é divisivel pelo contador
        print("\033[36m", end=' ')
        tot = tot + 1
    else:
        print("\033[31m", end=' ')
    print("{}".format(c),end=' ')
print("\n\033[mO numero {} foi divisivel {} vezes".format(num, tot))
if tot == 2: #se o total é divisivel por 2
    print("E por isso ele é PRIMO")
else:
    print("E por isso ele NÂO é primo")