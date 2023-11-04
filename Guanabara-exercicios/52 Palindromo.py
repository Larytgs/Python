print("É PALINDROMO? (\033[31mfrases/palavras que se podem ler, indiferentemente, da esquerda para a direita ou vice-versa.)")
frase = str(input("\033[mDigite uma frase: ")).strip().upper()
palavras = frase.split() #dividir as palavras, p formar uma lista
junto = ''.join(palavras) #juntou a lista numa string só
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1): #foi da ultima letra p primeira, voltando um letra
    inverso += junto[letra] #feito o inverso'''
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto: #print(junto, inverso)
    print("\033[34mTemos um Palimdromo!")
else:
    print("\033[31mA frase digitada NÂO é um Palindromo")
    #print("Voce digitou a frase {}".format(junto))


'''Frases:
ANOTARAM A DATA DA MARATONA
O LOBO AMA O BOLO
A TORRE DA DERROTA
APOS A SOPA'''