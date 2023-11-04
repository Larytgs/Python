def somar(a=0, b=0, c=0): #def somar(a, b, c): #desse jeito vai dar erro, pois n tem todos os numeros la em baixo
    '''
    Faz a soma de 3 valores, e mostra na tela
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    '''
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)           #parametros opcionais: colocando =0 na frente
somar(8, 4)
somar()

help(somar)
