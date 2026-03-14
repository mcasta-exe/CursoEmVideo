lista_indiv = list()
lista_geral = list()
lista_pessoas_maior = []
lista_pessoas_menor = []


while True:
    nome = str(input("Digite seu nome: ")).strip().capitalize()
    peso = float(input("Digite seu peso: "))
    lista_indiv.append(nome)
    lista_indiv.append(peso)
    lista_geral.append(lista_indiv[:])
    lista_indiv.clear()

    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper()
        if continuar in ("S","N"):
            break
        print('Entrada inválida!')
    if continuar == 'N':
        break

print(f"O número de pessoas cadastradas foi {len(lista_geral)}")

maior_peso = lista_geral[0][1] #O MAIOR PESO VAI SER DA PRIMEIRA PESSOA DA LISTA
menor_peso = lista_geral[0][1] #O MENOR PESO VAI SER DA PRIMEIRA PESSOA DA LISTA
# MAIOR E MENOR PESO
for pessoa in lista_geral:
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
# ATRIBUINDO O PESO AO NOME
for pessoa in lista_geral:
    if pessoa[1] == maior_peso:
        lista_pessoas_maior.append(pessoa[0])
        #print(pessoa[0])
    if pessoa[1] == menor_peso:
        lista_pessoas_menor.append(pessoa[0])


print(f"O maior peso registrado foi {maior_peso} kgs e pertence a {', '.join(lista_pessoas_maior)}")
print(f"o menor peso registrado foi {menor_peso} kgs e pertence a {', '.join(lista_pessoas_menor)}")