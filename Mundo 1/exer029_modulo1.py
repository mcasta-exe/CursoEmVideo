vel = float(input("Digite a velocidade do carro: "))
multa = (vel - 80.0) * 7.00
if vel > 80.0:
    print ("Você ultrapassou o limite de velocidade!")
    print("O valor da multa é de {:.2f} reais" .format(multa))
else:
    print("Você está dentro do limite de velocidade!")

