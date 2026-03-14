def fatorial(n=1, show=0):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == 1:
            print(c, end=' ')
            if c > 1:
                print("x", end=' ')
            else:
                print("=", end=' ')
    return f

num = int(input("Digite o numero que deseja saber o fatorial: "))
mostrar = int(input("Deseja visualizar os termos? [0 = Não], [1 = Sim]: "))
print(fatorial(num, mostrar))