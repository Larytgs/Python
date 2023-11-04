def contador(i, f, p):         #ex do exercicio 112
    '''
    ->Faz uma contagem e mostra na tela.
    :param i: incio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print("FiM")


#contador(2, 10, 2)
help(contador)

# docstrings
# Serve para ajudar o programador ou o usuário que estiver
# programando a minha funcionalidade