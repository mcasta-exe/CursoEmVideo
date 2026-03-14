n = 1
soma = 0
contador = 0
lista = []
while n != 0:
    n = int(input("Digite um número inteiro: "))
    k = str(input("QUER CONTINUAR? [S/N]: ")).upper().strip()
    soma += n
    contador += 1
    lista.append(n)
    if k != "S":
        break
media = soma / contador
print("A SOMA dos valores foi de {}\n"
      "A MÉDIA de todos os valores foi de {}\n"
      "O MAIOR valor foi {}\n"
      "O MENOR valor foi {}\n".format(soma,media, max(lista), min(lista)))