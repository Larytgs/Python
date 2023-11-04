
def arquivoExixte(msg):
    try:
        a = open('nome', 'rt') #rt: arquivo em modo texto
        a.close()
    except FileNotFoundError: #se o arquivo n foi encontrado
        return False
    else:
        return


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #escrever um arquivo de texto
        a.close()             #o '+' sig: se o arquivo n existir, ele cria
    except:
        print('Houve um erro, na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        print('-'*42)
        print("           Pessoas cadastradas")
        print('-' * 42)
        print(a.readlines())

