from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.Txt'

if not arquivoExixte(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastrar', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31m    ERRO! Digite uma opçao valida!\033[m')
    sleep(2)