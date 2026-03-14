from rich import print
from rich.table import Table


nome = 'jose'
tabela = Table(title= "Tabela de preços", width= 50, style='yellow')

tabela.add_column(f"{nome}", justify="right", style='purple')
tabela.add_column('quantidade', justify="center", style='green', width=20)
tabela.add_column('valor', justify='center',style='red')
tabela.add_row('lápis', "2x", "R$ 1,50")

print(tabela)