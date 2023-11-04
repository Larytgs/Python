try:
    a = int(input('Numerador: '))
    b = int(input('Deminador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Nao é possivel dividir um numero por 0.')
except KeyboardInterrupt:
    print('\nO usuario preferiu nao informaros dados.')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')
