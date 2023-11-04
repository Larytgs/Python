pessoas = {'nome': 'Laryssa', 'idade': 24, 'sexo': 'F'}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
pessoas['nome'] ='Joana'
pessoas['peso'] = 50.5
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')