estado = {}
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) #para copiar os dados do estado
#print(brasil)                    #para a lista brasil
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
print()
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
