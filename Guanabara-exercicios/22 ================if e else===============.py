'''nome = str(input("Escreve o seu nome: "))
if nome == 'Laryssa':
    print("Que nome lindo voce tem")
else:
    print("Seu nome é tao comum")
print("Bom dia {}".format(nome))'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2) / 2
print("Sua media é: {:.2f}".format(media))
if  media >= 6.0:
    print("Esta a cima da média, parabens!")
else:
    print("Esta a baixo da média, estude mais")