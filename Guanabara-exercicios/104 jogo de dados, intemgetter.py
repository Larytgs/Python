from random import randint
from time import sleep
from operator import itemgetter #
jogo = {"Jogador1": randint(0, 10),
        "Jogador2": randint(0, 10),
        "Jogador3": randint(0, 10),
        "Jogador4": randint(0, 10)
}
ranking = list()
print(" === OS VALORES SORTEADOS ===")
for k, v in jogo.items():
    print(f"  {k} tirou {v} no dado.")
    sleep(1)
print("="*31)
print(" === RANKING DOS JOGADORES ===")
ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"  {i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)
