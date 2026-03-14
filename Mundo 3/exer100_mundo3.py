from random import randint

def sorteia(n):
    print("Os números aleatórios gerados foram: ", end ='')
    for i in range(5):
        numb = randint(0, 100)
        numeros.append(numb)
        print(f"{numb} ", end ='')
    print()


def somaPar(s):
    somador = 0
    for p, s in enumerate(numeros):
        if s % 2 == 0:
            somador += s
    print(f"A soma dos números pares é igual a {somador}!")



numeros = []
sorteia(numeros)
somaPar(numeros)

