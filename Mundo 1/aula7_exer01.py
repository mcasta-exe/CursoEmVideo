n1 = int(input ("digite um número: "))
n2 = int(input ('digite outro numero: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
s1 = n1-n2
d1 = n1/n2
p = n1*n2
print (" a soma é {}, a divisão é {:.3f} e a multiplicação é {}".format(s, d, m), end = ' ')
print (" a subtração é {}, a divisão (de novo?) é {} e a multiplicação é {}" .format(s1, d1, p))