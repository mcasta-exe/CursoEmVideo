a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 0
while c < 10:
    pa = a1 + c * r
    c +=1
    print ("O {}° termo dessa PA cujo primeiro termo é {} e razão {} é {}".format(c,a1, r, pa))

