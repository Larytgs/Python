def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(8, 4, 2)
r2 = somar(2, 5)
r3 = somar(4)
print(f'A soma deles são: {r1}, {r2} e {r3}')
print('=-' * 20)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


print('    FATORIAL')
n = int(input("Digite um numero: "))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
print('=-' * 20)
print("  Fatorial de 5, 8 e 1")
f1 = fatorial(5)
f2 = fatorial(8)
f3 = fatorial() #vai fzr fatorial de 1, colocado la em cima
print(f'Os resultados são {f1}, {f2} e {f3}')

print('=-' * 20)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

print(' PARA ou IMPAR')
num = int(input('Digite um numero: '))
if par(num):
    print('È PAR!')
else:
    print('È IMPAR!')