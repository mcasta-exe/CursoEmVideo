print ("\033[1;31m        JOKENPÔ ONLINE      \033[m")
print('=='*15)
print ('')

# VARIABLE DECLARATION
rock = 'PEDRA!'
paper = 'PAPEL!'
scissors = 'TESOURA!'
lista = [rock,paper,scissors]
import random
machine = random.choice(lista)

#USER INTERFACE
user = str(input(' DIGITE 1 PARA PEDRA \n DIGITE 2 PARA PAPEL \n DIGITE 3 PARA TESOURA \n\n RESPOSTA: '))
print ('\033[1;31m         JO... KEN ... PÔ!\033[m   ')
print('=='*15)
if user == "1":
    print(" VOCÊ ESCOLHEU \033[1;32m PEDRA! \033[m")
elif user == "2":
    print(" VOCÊ ESCOLHEU \033[1;32m PAPEL! \033[m")
elif user == "3":
    print (" VOCÊ ESCOLHEU \033[1;32m TESOURA \033[m")

# MACHINE TURN
print (' E EU ESCOLHI ... ')
import time
time.sleep(2)
print ('\033[1;33m {}  \033[m'.format(machine))

# END GAME
if user == '1' and machine == paper:
    print ('\033[1;;44m EU VENCI! VOCÊ PERDEU! \033[m')
elif user == '1' and machine == scissors:
    print ('\033[1;;42m VOCÊ VENCEU! PARABÉNS! \033[m')
elif user == '2' and machine == rock:
    print ("\033[1;;42m VOCÊ VENCEU! PARABÉNS! \033[m")
elif user == '2' and machine == scissors:
    print("\033[1;;44m EU VENCI! VOCÊ PERDEU! \033[m")
elif user == '3' and machine == rock:
    print ("\033[1;;44m EU VENCI! VOCÊ PERDEU! \033[m")
elif user == '3' and machine == paper:
    print ("\033[1;;42m VOCÊ VENCEU! PARABÉNS! \033[m")
else:
    print ('\033[1;;40m EMPATAMOS! BOM JOGO! \033[m')