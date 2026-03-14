time = []
stats = []
while True:
    temp = []
    aproveitamento = {'nome_jogador': str(input("Digite o nome do jogador: ").capitalize()),
                      'gols': [], 'total': 0}

    partidas = int(input(f"Quantos jogos {aproveitamento['nome_jogador']} jogou?: "))
    temp.append(partidas)
    for n in range(partidas):
        gols = int(input(f"Quantos gols ele fez na {n+1}ª partida?: "))
        aproveitamento['gols'].append(gols)
        aproveitamento['total'] += gols
        temp.append(gols)
    time.append(aproveitamento)
    stats.append(temp)

    while True:
        resp = str(input("Quer continuar cadastrando [S/N]?: ")).upper()
        if resp in ("S","N"):
            break
        print("Resposta inválida")
    if resp == 'N':
        break

print(time)
print('=*=' *20)
texto = str("ID")
texto2 = str("Nome")
texto3 = str ("Gols Marcados")
texto4 = str("Total")
print(f"{texto.ljust(0)}", end = '')
print(f"{texto2.center(15)}", end='')
print(f"{texto3.rjust(15)}", end = '')
print(f"{texto4.center(15)}")
print('-'*50)
for pos, k in enumerate(time):
    print(f"{pos:<} {k['nome_jogador']:^15} {str(k['gols']):^15} {k['total']:^12}   ")

print('-'*50)

while True:
    data = int(input("Deseja visualizar as estatísticas de qual jogador? Digite 999 para parar. \n"
                        "Código: "))
    print("Digite 999 para parar")
    if data == 999:
        break
    if data >= len(time):
        print(f"ERRO")
    else:
        print(f"Estatísticas do jogador {time[data]['nome_jogador']}")
        for i, g in enumerate(time[data]['gols']):
            print(f" Na partida {i+1} fez {g} gols")
