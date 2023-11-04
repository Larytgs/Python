ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? (S/N) ")).strip().upper()
    if resp in 'Nn':
        break
print("-"*50)
print(f'{"No.":<4}{"NOME":<7}{"MEDIA":>6}')
print("="*25)
for indice, aluno in enumerate(ficha): #mostrar os dados
    print(f'{indice:<4}{aluno[0]:<7}{aluno[2]:>6.1f}') #nas msms posiçoes em cima
while True:
    print("="*30)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999: #opc é o numero do aluno
        print("FINALIZANDO")
        break
    if opc <= len(ficha) - 1:
        print(f"Nota de {ficha[opc][0]} sao {ficha[opc][1]}")
print("VOLTE SEMPRE!")
