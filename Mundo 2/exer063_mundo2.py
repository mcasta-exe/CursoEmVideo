n = int(input("Quantos termos da sequencia de FIBONACCI você deseja visualizar?:  "))
t0 = 0
t1 = 1
c = 3
print ("{}, {}, ".format(t0, t1), end = '')
while n >= c:
    t2 = t0 + t1
    print ("{}, ".format(t2), end ='')
    c +=1
    t0 = t1
    t1 = t2
print("[...]")