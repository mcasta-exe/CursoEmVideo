def ficha(nome="<desconhecido>", gols=0):
    return f"O jogador {nome} fez {gols} gols nessa temporada"

nome_jogador = str(input("Nome do jogador: ")). capitalize()
n_gols =  str(input("Gols feitos na temporada: "))
if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0
if nome_jogador.strip() == '':
    print(ficha(gols=n_gols))
else:
    print(ficha(nome_jogador,n_gols))

