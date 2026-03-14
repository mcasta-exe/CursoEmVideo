def aumentar(n=0, aum=0, f = False):

    if f:
        return moeda(aumentar(n), True)
    return n + (n * aum / 100)

def diminuir (n=0, desc=0, f = False):
    if f:
        return moeda(diminuir(n), True)
    return n - (n * desc / 100)

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

def resumo(price,aum,desc):
    print("-"*40)
    print("RESUMO DE VALORES".center(40))
    print("-" * 40)
    print(f"Preço analisado: \t\t{moeda(price)}")
    print(f"Dobro do preço: \t\t{moeda(dobro(price))}")
    print(f"Metade do preço: \t\t{moeda(metade(price))}")
    print(f"Com {aumentar(aum)}% de aumento: \t{moeda(aumentar(price,aum))}")
    print(f"Com redução de {diminuir(desc)}%: \t{moeda(diminuir(price, desc))}")
    print("-" * 40)