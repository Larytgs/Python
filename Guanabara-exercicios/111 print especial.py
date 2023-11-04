def escreva(msg):
    tam = len(msg) + 4 #o tamanho da mensagem, +4 é a borda(colocando mais 4 ~
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


escreva('Gustavo Guanabara')
escreva('Laryssa')
escreva('oi')