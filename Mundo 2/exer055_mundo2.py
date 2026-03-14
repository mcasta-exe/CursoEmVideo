lista = []
for c in range (1,6):
    weight = float(input("Digite o seu peso: "))
    lista.append(weight)
print ("O MAIOR PESO INSERIDO FOI DE {} kgs".format(max(lista)))
print ("O MENOR PESO INSERIDO FOI DE {} kgs".format(min(lista)))

# CASO EU QUISESSE UMA LISTA ORDENADA CRESCENTE:

#lista_ordenada = sorted(lista)
#print ("O MAIOR PESO INSERIDO FOI DE {} kgs".format(lista_ordenada[4]))
#print ("O MENOR PESO INSERIDO FOI DE {} kgs".format(lista_ordenada[0]))