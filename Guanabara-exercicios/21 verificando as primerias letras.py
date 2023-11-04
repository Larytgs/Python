#city = str(input("Em que cidade voce nasceu: ")).strip() #para tirar todos os espaços inuteis
#print(city[:5].upper() == 'SANTO') #para nao dar erro se colocarem letra minusculaou maiuscula

#nome = str(input("Qual o seu nome completo? ")).strip()
#print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))

frase = str(input("Escreva uma frase: ")).strip().upper()
letras = frase.count('A')
ultima = frase.rfind('A') #procure a partir do lado direito
print("A letra A aparece {} vezes na frase.".format(letras))
print("A primeira letra A apareceu na posição {}.".format(frase.find('A')))
print("A ultima letra A apareceu na posição {} ".format(ultima))