print((f'{" PALAVRAS e suas VOGAIS ":=^40}'))
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO','GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras: #vai analizar cada palavra da tupla
    print(f'\nNa palavra {p} temos ', end='  ')
    for letra in p:
        if letra.lower() in 'aáãeéiíoóõuú':
            print(letra.lower(), end=' ')