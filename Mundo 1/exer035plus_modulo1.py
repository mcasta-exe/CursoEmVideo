r1 = float(input("Digite o valor do primeiro seguimento de reta: "))
r2 = float(input("Digite o valor do segundo seguimento de reta: "))
r3 = float(input("Digite o valor do terceiro seguimento de reta: "))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1==r2 and r1==r3:
        print("Os seguimentos de reta formam um triângulo EQUILÁTERO")
    if r1==r2 or r2==r3 or r3==r1:
        print("Os seguimentos de reta formam um triângulo ISÓSCELES")
    if r1!=r2 and r2!=r3 and r3!=r1:
        print("Os seguimentos de reta formam um triângulo ESCALENO")
    if (r1**2 + r2**2) == (r3**2):
        print("Os seguimentos de reta formam um triângulo RETÂNGULO")
else:
    print('Os seguimentos de reta NÃO formam um triângulo!')