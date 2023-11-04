def teste(b):
    a = 7
    b += 4  #o A + B 5+2= 7
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro recebe {b}')
    print(f'C dentro recebe {c}')


a = 5
teste(a)
print('=' * 20)
print(f'A fora recebe {a}')