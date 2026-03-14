nome = str(input('Digite seu nome: ').strip())
n1=nome.split()
print(' O seu primeiro nome é {}'.format(n1 [0]))
print(' O seu último nome é {}'. format(n1[len(n1)-1])) # len Dentro de colchetes, pois, já está na função split