print(f'{"Numeros entre 0 e 20 por extenso":=^50}')
numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
          'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito'
          'dezenove', 'vinte')
while True:
    escolhido = int(input("Escolha um numero ente 0 e 20: "))

    if 0 <= escolhido <= 20:
        break
    print("Tente novamente. Digite um numero entre 0 e 20: ")
print(f"Voce digitou o numero {numero[escolhido]}")
