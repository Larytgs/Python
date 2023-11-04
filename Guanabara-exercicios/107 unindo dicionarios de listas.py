pessoa = {}
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    pessoa['sexo'] = str(input("Sexo [F/M]: ")).strip().upper()
    while pessoa['sexo'] not in 'FfMm':
        pessoa['sexo'] = str(input("\033[31mERRO! Responda apenas com F ou M: \033[m")).upper().strip()
    galera.append(pessoa.copy()) #copiar o dicionario dentro da lista
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    while resp not in 'SsNn':
        resp = str(input("\033[31mERRO! Responda apenas com S ou N: \033[m")).upper().strip()
    print('-'*40)
    if resp == 'N':
        break
print('=-'*80)
print(galera)
print(f"a) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"b) A média de idade é de {media:5.2f} anos.")
print(f"c) As mulheres cadastradas foram: ", end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']} ", end='')
print()
print(f"d) Lista das pessoas que estao acima da media: ")
for p in galera:
    if p['idade'] >= media:
        #print('     ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print('\033[35m<< ENCERRADO >>\033[m')