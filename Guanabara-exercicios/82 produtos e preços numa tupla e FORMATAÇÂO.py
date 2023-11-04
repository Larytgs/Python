listagem = ('Lapis', 1.75,
            'Borracha', 2.80,
            'Caderno', 15.90,
            'Estojo', 8.00,             #FORMATAÇÂO:
            'Compaso', 4.50,
            'Mochila', 30.99,
            'Caneta', 3.00,
            'Livro', 25.90)
print("-"*40)
print((f'{"LISTAGEM DE PREÇOS":=^40}'))
print("-"*40)
for posição in range(0, len(listagem)): #vai começar na posição 0 ate o tamanho da lista
    if posição % 2 == 0: #se a posição for par, vai mostraronome do protudo
        print(f"{listagem[posição]:.<30}", end='') #pontinhos alinhadas na esquerda
    else: #se a posição for impar, vai aparecer os valores
        print(f"R${listagem[posição]:>6.2f}") #.2f em duas casas decimais
print("-"*40)                                 #alinhado a direita