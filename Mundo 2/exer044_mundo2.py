print ("CALCULADORA DE PREÇO")

pro = float(input("Digite o valor do produto: "))
cash = pro*0.9 #in cash 10% off
cc1 = pro*0.95 #credit card 5%
cc2 = pro #credit card 2x
cc3 = pro*1.2 #credit card 3x or more

op1 = str(input("Qual será a opção de pagamento? \n Digite 1 para EM ESPÉCIE \n Digite 2 para CARTÃO \n"))
if op1 == "1":
    print("O VALOR TOTAL DA SUA COMPRA FOI DE R$ {:.2f}".format(cash))
elif op1 == "2":
    op2 = str(input("Irá parcelara sua compra? \n Digite 1 para SIM e 2 para NÃO \n"))
    if op2 == "2":
        print ('O VALOR DA SUA COMPRA FOI DE R$ {:.2f}'.format(cc1))
    elif op2 == "1":
        op3 = str(input(" Para dividir em 2x aperte 1 \n Para dividir em 3x aperte 2 \n"))
        if op3 == "1":
            print("O VALOR TOTAL DA SUA COMPRA FOI DE R$ {:.2f}".format(cc2))
        else:
            print ("O VALOR TOTAL DA SUA COMPRA FOI DE R$ {:.2f}".format(cc3))

