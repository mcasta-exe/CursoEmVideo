s1 = 0 #maior de 18
s2 = 0 #menor de 18

import datetime
current_year = datetime.date.today().year
for c in range(1,8):
    born = int(input("Digite o ano de nascimento da {}ª pessoa: ". format(c)))
    if current_year - born >= 18:
        s1+=+1
    else:
        s2+=+1
print ("A quantidade de pessoas maior de 18 anos é {}".format(s1))
print ("A quantidade de pessoas menores de 18 anos é {}".format(s2))

