from time import sleep
def contador(i, f, p): #inicio, fim e passo
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 35)
    print(f"Contagem de {i} ate {f} de {p} em {p}:")
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.5)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.5)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 35)
print('Agora é a sua vez de personalizar acontagem.')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)