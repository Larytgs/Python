def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos. NAO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos. Voto Opcional'
    else:
        return f'Com {idade} anos. Voto OBRIGATÒRIO!'


print(voto(2005)) #q tem 18 anos
print(voto(2015))
print(voto(1956))
nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))