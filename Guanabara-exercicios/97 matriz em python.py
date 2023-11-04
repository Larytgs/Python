matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #3x3
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um numero para [{linha}, {coluna}]: "))
print("-="*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print() #precisa para quebrar a linha da coluna


#o 1º for, é de alimentação, p colocar os numeros dentro da matriz
#o 2º for, são estrura de repetição, para mostrar a estrutura na tela