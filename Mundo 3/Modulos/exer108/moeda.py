def aumentar(n=0):
    return n + (n*10/100)

def diminuir (n=0):
    return n * 0.85

def dobro(n=0):
    return n*2

def metade(n=0):
    return n/2

def moeda(n=0):
    return f"R$ {n:.2f} reais".replace('.',',')