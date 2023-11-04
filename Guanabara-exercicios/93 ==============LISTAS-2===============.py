teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste[:]) #fazer uma cópia do teste, c outros dados
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])    #se nao tiver [:], vai repetir os dados
print(galera)
print('='*30)
classe = [['Matheus', 26], ['Laryssa', 24], ['Sara', 16], ['Giullia', 16]]
print(classe)
print(classe[1])
print(classe[3][0])
print(classe[0][1])
print(classe[2])
print('='*30)
for c in classe:
    #print(c)
    print(f'{c[0]} tem {c[1]} anos de idade.')