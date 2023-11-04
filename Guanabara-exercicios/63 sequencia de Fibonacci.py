print("Sequencia de FIBONACCI (\033[31msoma do numero anterior começanco com 0 dps 1\033[m)")
print("\033[36mExemplo: 0 -> 1 -> -> 2 -> 3 -> 5 -> 8 -> 13...\033[m")
print("=-"*25)
n = int(input("Quantos termos voce quer mostrar: "))
t1 = 0
t2 = 1
print("{} -> {}".format(t1, t2),end='')
cont = 3 #pq ja mostramos ate o 3
while cont <= n:
    t3 = t1 + t2
    print(" -> {}".format(t3),end='')
    t1 = t2 #t1 passa a ser o t2
    t2 = t3 #t2 passa a ser o t3...
    cont += 1
print(" -> FIM")