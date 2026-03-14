#PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO INTEIRO ESCOLHIDO PELO COMPUTADOR.
#O PROGRAMA DEVERÁ SINALIZAR AO USUÁRIO SE ELE ACERTOU OU ERROU

import random
n = int(input('Digite um número: '))
escol = random.randint(1, 5)
print("O número escolhido foi {}".format(escol))
if escol == n:
    print ("Você acertou o número! Parabéns!")
else:
    print ("Você não acertou o número!")

