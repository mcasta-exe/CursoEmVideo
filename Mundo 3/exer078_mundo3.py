lista = []

for i in range(5):
    n = float(input("Digite um valor: "))
    lista.append(n)

maior = max(lista)
menor = min(lista)

print(f"O maior valor foi {maior} nas posições:", end=" ")

for i, valor in enumerate(lista):
    if valor == maior:
        print(i, end=" ")

print(f"\nO menor valor foi {menor} nas posições:", end=" ")

for i, valor in enumerate(lista):
    if valor == menor:
        print(i, end=" ")

