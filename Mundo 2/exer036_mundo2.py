print('\033[1;33m     OLÁ, BEM VINDO AO NOSSO SISTEMA DE EMPRÉSTIMOS!     \033[m')
print('=='*30)
print('\033[1;31m     PARA APROVAR O EMPRÉSTIMO DO SEU IMÓVEL, PRECISO DE ALGUMAS INFORMAÇÕES: \n \033[m')
valor = float(input("Valor do imóvel que deseja adquirir: R$ "))
sala = float(input("Salário do comprador: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))
print("     OBRIGADO PELAS INFORMAÇÕES!     ")
print("     AGUARDE ENQUANTO REALIZAMOS OS CÁLCULOS...")
import time
time.sleep(3)
presta = valor / anos #prestação anual
prestm = presta/12 #prestação mensal
print('    \033[1;32m DE ACORDO COM NOSSOS CÁLCULOS O VALOR DA SUA PRESTAÇÃO MENSAL É DE R$ {:.2f} \033[m'. format(prestm))
if prestm > 0.3*sala:
    print ('    \033[1;31m      SUA PRESTAÇÃO EXCEDE 30% DO SEU SALÁRIO (R$ {:.2f})   \033[m'.format(0.3*sala))
    print ('    \033[1;31m      SEU EMPRÉSTIMO FOI NEGADO!   \033[m')
else:
    print('     \033[1;31m      PARABÉNS, SEU EMPRÉSTIMO FOI APROVADO!      \033[m\n')
print('    \033[1;;43m ATENDIMENTO ENCERRADO \033[m      ')
print('=='*30)