print ("CALCULADORA DE MÉDIAS")
score1 = float(input("digite a nota da primeira avaliação: "))
score2 = float(input('digite a nota da segunda avaliação: '))
avr = (score1 + score2)/2
if avr >= 7:
    print ('VOCÊ ESTÁ APROVADO, SUA MÉDIA FOI DE {:.2f}'.format(avr))
elif avr < 5:
    print ("VOCÊ ESTÁ REPROVADO, SUA MÉDIA FOI DE {:.2f}".format(avr))
elif 5 <= avr < 7:
    print("VOCÊ ESTÁ DE RECUPERAÇÃO, SUA MÉDIA FOI DE {:.2f}".format(avr))


