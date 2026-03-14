n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite um número inteiro [999 para parar]: "))
    cont += 1
    if n < 999:
        soma = soma + n

print("Foram digitados {} números e a soma deles foi de ".format(cont-1), soma)