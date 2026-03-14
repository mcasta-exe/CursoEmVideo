lista = list()
e = str(input("Digite uma expressão: "))
lista.append(e)

for i in lista:

    if i[0] == '(' and i[-1] == ')':
        print("Expressão correta.")
    else:
        print('Expressão inválida.')
