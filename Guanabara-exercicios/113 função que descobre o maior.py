from time import sleep

def maior(* num):
    cont = maior = 0
    print('=' * 20)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end= '')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi: {maior}')


maior(2, 9 , 6, 15, 5, 0)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
