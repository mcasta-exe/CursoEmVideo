option = ''
while option != '5':

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    print ("\n  \033[1:33m #### MENU #### \033[:31m\n"
           "[1] Somar\033[:32m\n"
           "[2] Multiplicar\033[:34m\n"
           "[3] Maior\033[:35m\n"
           "[4] Novos números\033[:36m\n"
           "[5] Sair\033[m")
    option = input("Selecione a opção desejada: ")

    if option == '1':
        soma = n1 + n2
        print("A soma dos números {:.2f} e {:.2f} é {:.2f}".format(n1, n2, soma))
    elif option == '2':
        mult = n1 * n2
        print("A multiplicação dos números {:.2f} e {:.2f} resulta em {:.2f}".format(n1, n2, mult))
    elif option == '3':
        if n1 > n2:
            print ("O maior número é {}".format(n1))
        else:
            print ("O maior número é {}".format(n2))
    elif option == '4':
        print(""
              "\033[::41m Escolha novamente: \033[m")


