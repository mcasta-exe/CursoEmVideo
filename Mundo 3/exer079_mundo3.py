lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado.")
    else:
        print("Valor duplicado! Não será adicionado.")
    while True:
        p = input("Deseja continuar? [S/N] ").strip().upper()
        if p in ("S", "N"):
            break
        print("Entrada inválida!")
    if p == "N":
        break
lista.sort()
print(f"Lista final: {lista}")
