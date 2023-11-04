print("{:=^40}".format(' LOJAS LARYSSA '))
preço = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque 
[ 2 ] À vista cartao 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão ''')

opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100) #10% de desconto
elif opção == 2:
    total = preço - (preço * 5 / 100) #5% de desconto
elif opção == 3:
    total = preço #preço normal
    parcela = total / 2
    print("Sua compra sera parcelada em 2x de R${} SEM JUROS.".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100 ) #20% de juros
    totalparc = int(input("Quantas parcelas? "))
    parcela = total / totalparc
    print("Sua compra sera parcelado em {}x de R${:.2f} COM JUROS.".format(totalparc, parcela))
else:
    total = 0
    print("\033[31mOPÇAO INVALIDADE de parcelas. Tente novamente!\033[m")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))
