from datetime import date
print("Analisar a idade da pessoa se é maior ou menor de idade")
atual = date.today().year #data atual
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor = totmenor + 1
print("E tambem tivemos {} pessoas maiores de idade.".format(totmaior))
print("E tambem tivemos {} pessoas menores de idade.".format(totmenor))
