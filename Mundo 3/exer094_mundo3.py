pessoas = []
soma_i = 0
mulheres = []

while True:
    dados = {}

    dados['nome'] = input("Digite seu nome: ")
    dados['idade'] = int(input("Digite sua idade: "))
    soma_i += dados['idade']

    while True:
        dados['sexo'] = input("Digite seu sexo [M/F]: ").upper()
        if dados['sexo'] in ("M", "F"):
            if dados['sexo'] == "F":
                mulheres.append(dados['nome'])
            break
        print("Resposta inválida")
    pessoas.append(dados)

    while True:
        resp = input("Deseja continuar? [S/N]: ").upper()
        if resp in ("S", "N"):
            break
        print("Resposta inválida")

    if resp == "N":
        break

print(pessoas)
print(f"A quantidade de pessoas cadastradas foi de {len(pessoas)} pessoas")

media_idade = soma_i/len(pessoas)

print(f"A média das idades dessa população é de {media_idade:.2f} anos")
print(f"O nome das mulheres cadastradas foram: {mulheres}".replace(',', ' e'))

acima_media = []
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa['nome'])
print(f" Acima da idade média somente: {acima_media}".replace(',', ' e'))
