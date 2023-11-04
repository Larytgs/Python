'''def lin():
    print('='*20)

lin()
print(f"{'Python':^20}")
lin()
print(f"{'Mundo':^20}")
lin()
print(f"{'Guanabara':^20}'''

'''def titulo(txt):
    print('='*20)
    print(txt)
    print('='*20)


titulo('Curso em video')
titulo('Python')'''

a = 4
b = 3
soma = a + b
print(soma)
a = 5
b = 4
soma = a + b
print(soma)

print()
def soma(a, b):
    print(a+b)


soma(4, 3)
soma(5, 4)
soma(9, 9)

print()
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f"A soma de A + B = {s}")


soma(5, 7)
soma(8, 9)

print()
def contador(*num): #o * pega todos os numeros q estiver no contador
    s = 0
    for n in num:
        s += n
    print(f"Somando os valores {num} temos {s}")
    tam = len(num)
    print(f"Recebi os valor {num} e sao ao todo {tam} numeros.")
    print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2 #vai multiplicar por ele mesmo
        pos += 1


valores = [5, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)