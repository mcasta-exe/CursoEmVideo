lista = []
cont = 0
cont5 = 0
while True:
    n=lista.append(int(input("Digite um valor: ")))
    cont += 1

    while True:
        p = str(input("Deseja continuar? [S/N] ")).strip().upper()
        if p in ("S","N"):
            break
        else:
            print("Entrada inválida")
    if p == "N":
        break
if 5 in lista:
    cont5 += 1
    print(f"O valor 5 apareceu na lista {cont5} vezes.")

else:
    print("Não foi inserido nenhum número 5 na lista.")

print(f'A quantidade de valores na lista é de {cont}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')