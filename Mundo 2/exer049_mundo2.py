num = int(input("Escolha um número inteiro qualquer: "))
print ("A tabuada deste número é: ")
for c in range(1, 11):
    print ("{} x {} = {}".format(num, c, num * c))
