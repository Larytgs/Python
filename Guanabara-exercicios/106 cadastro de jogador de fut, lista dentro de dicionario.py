from time import sleep
jogador = {}
partidas = list()
jogador['nome'] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for c in range(0, total):
    partidas.append(int(input(f"  Quantos gols na partida {c+1}? ")))
jogador['gols'] = partidas[:] #o jogador, vai receber uma copia de partidas
jogador['total'] = sum(partidas) #somar
print("="*30)
print(jogador)
sleep(1)
print("="*30)
for k, v in jogador.items():
    print(f"  => O campo {k} tem o valor {v}")
print("="*30)
sleep(2)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
