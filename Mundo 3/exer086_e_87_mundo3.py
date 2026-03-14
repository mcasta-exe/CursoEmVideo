matriz = []
valores = [[],[],[]]
pares = []
terceira = []

for l in range(0,3):
    for c in range(0,3):
        n = int(input(f"Digite um valor para [{l},{c}]: "))
        if l == 0:
            valores[0].append(n)
        if l == 1:
            valores[1].append(n)
        if l == 2:
            valores[2].append(n)
        if n % 2 == 0:
            pares.append(n)
        if c == 2:
            terceira.append(n)


matriz.append(valores[0])
matriz.append(valores[1])
matriz.append(valores[2])

print(f" [ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ] \n"
      f" [ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ] \n"
      f" [ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]")

# PARES
print(f"A soma dos valores pares da matriz é: {sum(pares)}.")
# TERCEIRA COLUNA
print(f"A soma dos valores da 3ª coluna é {sum(terceira)}.")
# MAIOR VALOR DA 2ND COLUNA
maior = max(valores[1])
print(f"O maior valor da 2ª linha foi {maior}.")