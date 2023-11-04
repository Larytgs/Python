def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n

def leifloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero real.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuario.\033[m')
            return 0
        else:
            return n


n1 = leiaint("Digite um valor inteiro: ")
n2 = leifloat('Digite um numero real: ')
print(f'O valor inteiro foi \033[34m{n1}\033[m e o valor real foi \033[34m{n2}\033[m')