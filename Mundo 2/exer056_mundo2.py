lista_idade = []
lista_masculino = []
lista_feminino = []
lista_masc_idade = []
lista_fem_idade = []
s=0

for c in range (0,4):
    name = str(input('Digite seu nome: ')).strip().upper()
    age = int(input('Digite sua idade: '))
    sex = str(input('Digite seu sexo: ')).strip().upper()
    print('-='*15)
    lista_idade.append(age)
    lista_masc_idade.append(age)
    lista_fem_idade.append(age)
    if sex == "MASCULINO":
        lista_masculino.append(name)
    else:
        lista_feminino.append(name)

lista_masc_idade_org=sorted(lista_masc_idade)
print("O nome do homem mais velho é {} e ele tem {} anos".format(lista_masculino,lista_masc_idade_org[-1]))

lista_fem_idade_org = sorted(lista_fem_idade)
if any ( n < 20 for n in lista_fem_idade_org):
    s+=+1
print('O número de mulheres com menos de 20 anos é {}'. format(s))

avr_age = sum(lista_idade)/4 #média das idades do grupo
print('A média da idade desse grupo é de {} anos'.format(avr_age))


