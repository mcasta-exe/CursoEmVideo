print("=" *20, "MEGA SENA", "="* 20)

import random
import time

total_jogos = []
qtd_jogos = int(input("Quantos jogos deseja gerar? "))

for s in range(0, qtd_jogos):
    cartela = []
    total_jogos.append(cartela)
    while len(cartela) < 6:
        gerador = random.randint(1, 60)
        if gerador not in cartela:
            cartela.append(gerador)
        cartela.sort()

for c in range(0, qtd_jogos):
    print(f"Jogo número {c+1} {total_jogos[c]}")
    time.sleep(1)
