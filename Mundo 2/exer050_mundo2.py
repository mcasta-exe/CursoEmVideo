s=0
for c in range(1, 7):
    number = int(input("Escolha um número inteiro: "))
    if number % 2 == 0:
        s += number
print ("A SOMA DOS NÚMEROS PARES É DE {}".format(s))

