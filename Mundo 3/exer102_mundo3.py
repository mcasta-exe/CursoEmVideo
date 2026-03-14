def fatorial(n=1, show=False):

    f = 1
    for c in range (n,0,-1):
        f *= c
        if show:
            print(c, end =' ')
            if c > 1:
                print("x", end=' ')
            else:
                print("=", end =' ')
    return f


print(fatorial(5,show=False))
