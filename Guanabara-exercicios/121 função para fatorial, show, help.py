def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um numero
    :param num: o numero a ser calculado
    :param show: mostrar ou nao a conta
    :return: o valor do fatorial de um numero num.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))
# chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
help(fatorial)