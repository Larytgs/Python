#USANDO O EXEMPLO DO 66:
n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")

#OUTRO EXEMPLO:
'''nome = 'Joana'
idade = 33
print(f"O {nome} tem {idade} anos") #PYHTON 3.6
print("O {} tem {} anos".format(nome, idade)) #PYTHON 3
print("O %s tem %d anos" % (nome, idade)) #PYHTON 2'''

'''nome = 'Laryssa'
idade = 24
salario = 1350.3
cidade = 'Curitiba'
print(f"A {nome} tem {idade} anos, com salario R${salario:.2f} e mora em {cidade}.")'''