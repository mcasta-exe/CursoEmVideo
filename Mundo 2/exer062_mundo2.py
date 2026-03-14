a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 0
while c < 10:
    pa = a1 + c * r
    c +=1
    print ("O {}° termo dessa PA cujo primeiro termo é {} e razão {} é {}".format(c,a1, r, pa))

perg = '1'

while perg == "1":
    print("Você deseja ver mais termos desta PA?")
    perg = str(input("[1] SIM \n"
                     "[0] NÃO\n"
                     "RESPOSTA: "))
    if perg == '0':
        print("FIM DO PROGRAMA")
    else:
        t1 = int(input("Quantos termos a mais para esta PA? "))
        c2 = c + t1
        while c < c2:
            pa = a1 + c * r
            c +=1
            print ("O {}° termo dessa PA cujo primeiro termo é {} e razão {} é {}".format(c,a1, r, pa))
