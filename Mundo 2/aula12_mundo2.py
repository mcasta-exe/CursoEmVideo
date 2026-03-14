nome = str(input("Digite seu nome completo: "))
if nome == 'Matheus':
    print("Seu nome é irado!")
elif nome == 'Maria' or nome == 'João':
    print("Seu nome é bem comum no Brasil.")
else:
    print("Seja bem vindo! {}".format(nome))