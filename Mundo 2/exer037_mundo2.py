print("BEM VINDO AO CONVERSOR DE NÚMEROS")
n = int(input ("Digite um número inteiro: "))
b = input("Qual será a base da conversão? \n Digite 1 para BINÁRIO \n Digite 2 para OCTAL \n Digite 3 para HEXADECIMAL \n RESPOSTA: ")
print ('REALIZANDO A CONVERSÃO DO NÚMERO...')
import time
time.sleep(3)
bi = bin(n)
oc = oct(n)
he = hex(n)
if b == '1':
    print ("O NÚMERO {} PODE SER REPRESENTADO PELO SISTEMA BINÁRIO COMO {}" .format (n,bi[2:]))
if b == '2':
    print ("O NÚMERO {} PODE SER REPRESENTADO PELO SISTEMA OCTAL COMO {}" .format (n,oc[2:]))
if b == '3':
    print ("O NÚMERO {} PODE SER REPRESENTEADO PELO SISTEMA HEXADECIMAL COMO {}" .format (n,he[2:]))
print('=='*30)