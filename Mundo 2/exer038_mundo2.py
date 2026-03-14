print ("\033[1;31m SISTEMA DE COMPARAÇÃO DE DOIS NÚMEROS \033[m")
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
if n1 > n2:
    print("O PRIMEIRO NÚMERO {} É MAIOR QUE O SEGUNDO {}".format(n1,n2))
elif n1 < n2:
    print ("O SEGUNDO NÚMERO {} É MAIOR QUE O PRIMEIRO {}".format(n2,n1))
elif n1 == n2:
    print ("OS DOIS NÚMEROS SÃO IGUAIS")