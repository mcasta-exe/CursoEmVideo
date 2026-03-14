num = int(input("Digite um número: "))
mult = 1
reg = num
while reg > 0:
    mult *= reg ## mult = mult * reg
    reg -= 1 #subtrai do reg anterior e guarda == reg = reg -1

print("O fatorial de {}! é igual a {}".format(num, mult))


#num = int(input("Digite um número: "))
#multiplicador = 1
#for c in range(num, 0, -1):
#    multiplicador *= c

#print(multiplicador)