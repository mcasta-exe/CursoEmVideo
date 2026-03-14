print ("    \033[1;31m INDICADOR DE ALISTAMENTO ONLINE \033[m     ")
born = int(input("Digite em que ano você nasceu: ")) # to turn 18 must have born in 2008
if born == 2008:
    print(" \033[1;31m VOCÊ DEVE SE ALISTAR ESTE ANO! \033[m")
elif born > 2008:
    print (" \033[1;31m FALTAM {} ANOS PARA SEU ALISTAMENTO OBRIGATÓRIO \033[m" .format(born-2008))
elif born < 2008:
    print(" \033[1;31m SEU ALISTAMENTO OCORREU {} ANOS ATRÁS, VÁ ATÉ A JUNTA MILITAR MAIS PRÓXIMA \033[m" .format(2008-born))
