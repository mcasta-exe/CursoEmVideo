print("CALCULADORA DE MASSA CORPORAL ONLINE")
he = float(input("Digite sua altura em metros: "))
we = float(input("Digite seu peso em kgs: "))
IMC = we/(he*he)
if IMC < 18.5:
    print('Seu IMC é {:.2f} e você está ABAIXO DO PESO'.format(IMC))
elif 18.5 <= IMC <= 25:
    print("Seu IMC é {:.2f} e você está no PESO IDEAL".format(IMC))
elif 25 <= IMC <= 30:
    print("Seu IMC é {:.2f} e você está com SOBREPESO".format(IMC))
elif 30 <= IMC <= 40:
    print("Seu IMC é {:.2f} e você está com OBESIDADE".format(IMC))
else:
    print ("Seu IMC é {:.2f} e você tem OBESIDADE MÓRBIDA".format(IMC))