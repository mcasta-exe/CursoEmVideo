n = str(input('Digite o nome completo da pessoa: ')).strip()
print(n.upper()) #Colocar tudo em maiúscula
print(n.lower()) #Colocar tudo em minúscula
print('Seu nome tem ao todo {} letras'.format(len(n)-n.count(' ')))
n1= n.split()
print ('Seu primeiro nome tem {} letras'.format(n1[0]), len(n1[0]))

