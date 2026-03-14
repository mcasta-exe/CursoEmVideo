valores = [[],[]]

for i in range(1,8):
    n = int(input(f"Digite o {i}º valor: "))
    if n % 2 == 0:
        valores[0].append(n)

    else:
        valores[1].append(n)

#num[0].sort()
#num[1].sort()
print(f" Pares {sorted(valores[0])} \n Ímpares {sorted(valores[1])}")

