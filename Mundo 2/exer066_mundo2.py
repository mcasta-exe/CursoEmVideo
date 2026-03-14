cont = 0
soma = 0
while True:
    n = int(input("Digite um valor [999 para interromper]: "))
    if n < 999:
        cont += 1
        soma += n
    if n == 999:
        break
print(f"A quantidade de termos foi {cont} e a soma foi {soma}")