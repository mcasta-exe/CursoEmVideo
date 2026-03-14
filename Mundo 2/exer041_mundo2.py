print ("OLÁ ATLETA, BEM VINDO(A)")
import datetime
current_year = datetime.date.today().year
y = int(input('Insira seu ano de nascimento: '))
age = current_year - y
print ("VOCÊ TEM {} ANOS".format(age))
print ("A CATEGÓRIA ADEQUADA PARA VOCÊ DE ACORDO COM SUA IDADE É: ")
if age <=9:
    print('MIRIM')
elif age <=14:
    print ('INFANTIL')
elif age <=19:
    print ('JÚNIOR')
elif age <=25:
    print('SÊNIOR')
else:
    print ("MASTER")
