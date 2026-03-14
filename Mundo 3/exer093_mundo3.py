aproveitamento = {'nome_jogador': str(input("Digite o nome do jogador: ").capitalize()),
                  'gols': [], 'total': 0}

partidas = int(input(f"Quantos jogos {aproveitamento['nome_jogador']} jogou?: "))

for n in range(partidas):
    gols = int(input(f"Quantos gols ele fez na {n+1}ª partida?: "))
    aproveitamento['gols'].append(gols)
    aproveitamento['total'] += gols

print('=*=' *20)
print(aproveitamento)
print('=*=' *20)

for k,v in aproveitamento.items():
    print(f"O campo {k} tem valor {v}")
print('=*=' *20)

print(f'O jogador {aproveitamento["nome_jogador"]} jogou {partidas} partidas')
for n,r in enumerate(aproveitamento['gols'], start = 1):
    print(f" => Na partida {n}, fez {r} gols")
print('=*=' *20)