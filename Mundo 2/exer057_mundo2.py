sex = ''
contador = 0
print("Digite M para Masculino ou F para Feminino")
print("Digite SAIR para encerrar")
while sex != 'SAIR':
    sex = str(input('Digite seu sexo [M/F]: ')).upper(). strip()
    if sex != 'M' and sex != 'F' and not sex =='SAIR':
        print("Apenas M ou F são aceitos como resposta!")
    elif sex in 'M, F':
        contador += 1
if sex == 'SAIR':
    print ("Encerrando")
print("A quantidade de gêneros registrados foi de {}".format(contador))