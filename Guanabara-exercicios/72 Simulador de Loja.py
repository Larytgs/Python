totcompra = maisde1000 = nomemenor = preçomenor = cont = 0
print("=-"*20)
print("{:=^40}".format('\033[35mLOJA SUPER BARATO\033[m'))
print("=-"*20)
while True:
    nome = str(input("Nome do produto: "))
    preço = float(input("Preço: R$"))
    cont += 1
    totcompra += preço
    if preço > 1000:
        maisde1000 += 1
    if cont == 1 or preço < preçomenor:
            preçomenor = preço
            nomemenor = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("\033[31mQuer contiuar? [S/N]\033[m ")).strip().upper()[0]
    if continuar == 'N':
        break
print("=-"*20)
print(f"\033[36mO total da compra deu: R${totcompra:.2f}")
print(f"Temos {maisde1000} produtos custando mais de R$1000,00.")
print(f"O produto mais barato foi {nomemenor} que custa R${preçomenor}.\033[m")