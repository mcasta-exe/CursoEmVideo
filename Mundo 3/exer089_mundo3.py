
cadastro_geral = []

while True:
    dados_aluno = list()
    notas_aluno = list()

    nome = str(input("Digite o nome do aluno: ")).strip().capitalize()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    dados_aluno.append(nome)
    notas_aluno.append(nota1)
    notas_aluno.append(nota2)
    notas_aluno.append(media)

    dados_aluno.append(notas_aluno)
    cadastro_geral.append(dados_aluno)


    while True:
        k = str(input("Deseja Continuar [S/N]? ")).upper()
        if k != "S" and k != "N":
            print("Digite S ou N")
        else:
            break
    if k == "N":
      break

print(cadastro_geral)

for c in range(0, len(cadastro_geral)):
    print("------------------------------- \n"
        f"ID: {c+1} \n"
          f"Nome: {cadastro_geral[c][0]} \n"
          f"Média: {cadastro_geral[c][1][2]}")
print("-------------------------------")

while True:
    v = str(input("Deseja ver as notas de algum aluno [S/N]?: ")).upper()
    if v != "S" and v != "N":
        print("Digite S ou N")
    if v == "S":
        q = int(input("Qual o ID do aluno? "))
        if q >= 1 or q <= len(cadastro_geral):
            print(f"1ª Prova: {cadastro_geral[q-1][1][0]} \n2ª Prova {cadastro_geral[q-1][1][1]}")
    else:
        break
