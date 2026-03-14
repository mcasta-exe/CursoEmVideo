import math
ca = float(input("Digite o valor do cateto adjacente: "))
co = float(input("Digite o valor do cateto oposto: "))
hi = math.hypot(ca, co)
print ("O valor da hipotenusa é: {:.2f}".format(hi))