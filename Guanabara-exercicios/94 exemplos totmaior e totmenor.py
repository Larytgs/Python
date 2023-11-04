galera = list()
dado = list() #vai pegar temporariamente a lista
totalmaior = totalmenor = 0
for c in range(0,4):
    dado.append(str(input("Nome: ")))
    dado.append((int(input("Idade: "))))
    galera.append(dado[:]) #vai jogar dentro da galera
    dado.clear() #vai excluir lista dado
print(galera)
for p in galera:
    if p[1] > 18:
        print(f"{p[0]}, tem {p[1]} anos, é maior de idade.")
        totalmaior +=1
    else:
        print(f"{p[0]}, tem {p[1]} anos, não é maior de idade.")
        totalmenor +=1
print(f"Temos {totalmaior} maior de idade, e {totalmenor} menor de idade")