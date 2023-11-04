jogador = {}
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f">Quantas gols na partida {c+1}? ")))
    print('-'*60)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
    while resp not in 'SsNn':
        resp = str(input("\033[31mERRO! Responda apenas com S ou N: \033[m")).upper().strip()
    if resp == 'N':
        break
print('=-'*40)
print('cod', end='') #analise de dados
for i in jogador.keys():
    print(f"{i:<15}", end='') #vai aparecer (cod nome gols total) na tabela
print()
print('=-'*40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print('=-'*40)
while True:
    busca = int(input("Mostra dados de qual valor: "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"\033[31mERRO! Nao existe jogador com codigo {busca}!\033[m")
    else:
        print(f" -- Levantamento do jogador {time[busca]['nome']}:")
        for i, q in enumerate(time[busca] ['gols']):
            print(f"  No jogo {i+1} fez {q} gols.")
        print('='*40)
print("\033[35mVolte sempre\033[m")