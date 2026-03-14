def aumentar(n=0, f = False):

    if f:
        return moeda(aumentar(n), True)
    return n + (n * 10 / 100)

def diminuir (n=0, f = False):
    if f:
        return moeda(diminuir(n), True)
    return n * 0.85

def dobro(n=0, f = False):
    if f:
        return moeda(dobro(n), True)
    return n*2

def metade(n=0, f = False):
    if f:
        return moeda(metade(n), True)
    return n/2

def moeda(n=0, f = True):
    if f:
        return f'R$ {n:.2f} reais'.replace('.', ',')
    return n