d = float(input("Qual a distância da sua viagem em km? "))
p1 = d*0.50 #até 200km
p2 = d*0.45 #acima de 200km
if d<=200:
    print ("O preço da sua passagem será de R${:.2f}".format(p1))
else:
    print ("O preço da sua passagem será de R${:.2f}".format(p2))