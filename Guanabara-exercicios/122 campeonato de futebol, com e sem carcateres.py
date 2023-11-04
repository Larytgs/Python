def ficha(jog='desconhecido', gol=0):
    print(f'o Jogador {jog} fez {gol} gols no campeonato.')



n = str(input('Nome do jogador: '))
g = str(input('Quantos gols? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '': #se tirei todos os espaços e ficou vazio:
    ficha(gol=g)
else:
    ficha(n, g)