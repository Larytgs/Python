'''import random
nome1 = input("Primeiro aluno: ")
nome2 = input("Segundo aluno: ")
nome3 = input("Terceiro aluno: ")
nome4 = input("Quarto aluno: ")
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))'''

from random import shuffle
nome1 = input("Primeiro nome: ")
nome2 = input("Segundo nome: ")
nome3 = input("Terceiro nome: ")
nome4 = input("Quarto nome: ")
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print("A ordem de apresentação sera: {}".format(lista))