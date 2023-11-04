def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço
    :param preço: o preço q quer se ajustar
    :param taxa: qual é a porcentagem de aumento
    :param formato: quer a saida formatado ou não?
    :return: o valor reajustado, com ou sem formato
    Esse é do exercicio 109
    Tem que colocar 'True' no outro codigo(109)
    '''
    resp = preço + (preço * taxa/100)
    return resp if not formato else moeda(resp)
    # se o preço n estiver com o formato, ele vai formatar c o comando moeda la em baixo


def diminuir(preço=0, taxa=0, formato=False):
    resp = preço - (preço * taxa/100)
    return resp if formato is False else moeda(resp)


def dobro(preço=0, formato=False):
    resp = preço * 2
    return resp if not formato else moeda(resp)


def metade(preço=0, formato=False):
    resp = preço / 2
    return resp if not formato else moeda(resp)

#fazer a formatação em reais, exercicio 108 no guanabara
def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',') #converter o ponto p virgula


def resumo(preço=0, taxaa=10, taxar=5):
    print('='*30)
    print('      RESUMO DO VALOR')
    print('='*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento:  \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de desconto:  \t{diminuir(preço, taxar, True)}')
    print('='*30)