def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"Erro, não é um número inteiro!")
        if ok:
            break
    return valor

num = leiaint(f"Digite um número inteiro: ")
print(f"O valor digitado foi {num}")