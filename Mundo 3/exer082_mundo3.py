Lista = list()
lista_par = list()
lista_imp = list()

while True:
    n = int(input("Digite um valor: "))
    Lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_imp.append(n)
    while True:
        p = str(input("Quer continuar? [S/N] ")).upper().strip()
        if p in ("S", "N"):
            break
        print("Resposta inválida")
    if p == "N":
        print("Lista encerrada.")
        break

print(f'A Lista inicial é: {Lista}')
print(f'A Lista de pares é: {lista_par}')
print(f'A Lista de ímpares é: {lista_imp}')
