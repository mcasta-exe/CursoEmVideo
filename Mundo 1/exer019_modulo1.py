import random
n1 = input("digite o primeiro nome: ")
n2 = input("Digite o segundo nome: ")
n3 = input("Digite o terceiro nome: ")
n4 = input("Digite o quarto nome: ")
lista = [n1, n2, n3, n4]
escol = random.choice(lista)
print ("o escolhido foi {}".format(escol))
