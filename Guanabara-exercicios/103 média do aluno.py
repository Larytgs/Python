alunos = {}
alunos['nome'] = str(input("Nome: "))
alunos['media'] = float(input(f"Média do {alunos['nome']}: "))
print("=-"*20)
#print(f"Nome é igual a {alunos['nome']}")
#print(f"Media igual a {alunos['media']}")
if alunos['media'] < 4:
    alunos['situação'] = 'REPROVADO'
elif 4 <= alunos['media'] < 7:
    alunos['situação'] = 'RECUPERAÇÃO'
elif alunos['media'] >= 7:
    alunos['situação'] = 'APROVADO'
print(alunos)
for k, v in alunos.items():
    print(f' -{k:.<10} = {v:>6}')


