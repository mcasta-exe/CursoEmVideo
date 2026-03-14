s = float(input("Qual o seu salário atual? R$ "))
a1 = s*1.10
a2 = s*1.15
if s>1250:
    print("Seu salário com aumento será de R$ {:.2f}" .format(a1))
else:
    print("Seu salário com aumento será de R$ {:.2f}" .format(a2))