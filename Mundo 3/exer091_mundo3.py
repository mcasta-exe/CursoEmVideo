from random import randint
from time import sleep

jogadas = {}

for c in range(4):
    jogadas[f'Jogador {c+1}'] = randint(1,6)

for jogador, v in jogadas.items():
    print(f"O {jogador} tirou {v}")
    sleep(1)

print("Ranking dos Jogadores:")

ranking = sorted(jogadas.items(), key=lambda item: item[1], reverse = True)

for posicao, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{posicao}º Lugar: {jogador} com {valor}")


