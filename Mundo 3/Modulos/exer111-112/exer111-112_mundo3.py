from utilitiescv import moeda
from utilitiescv import dado

valor = dado.leiadinheiro(f"Digite o preço: R$: ")
moeda.resumo(valor, 20, 50  )