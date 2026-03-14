import random
contador = 1
n_usuario = int(input("Digite um número entre 0 e 10: "))
n_machine = random.randint(0,10)

while n_usuario != n_machine:
    print('O número escolhido foi diferente do meu!')
    n_usuario = int(input("Escolha outro número entre 0 e 10: "))
    contador += 1
    if n_usuario == n_machine:
        print("\033[1;31m Você acertou, o número que escolhi foi {}\033[m".format(n_machine))

print("Você tentou acertar o número {} vezes!".format(contador))
