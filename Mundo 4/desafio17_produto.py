from rich.panel import Panel
from rich import print

class Produto:

    def __init__(self, name, price):
        self.nome = name
        self.preco = price

    def etiqueta(self):
        conteudo = f"{self.nome}".center(30,' ')
        conteudo += f"*"*len(conteudo)
        precof = f"R$ {self.preco:.2f}".replace('.',',')
        conteudo += precof.center(30, '.')
        etiqta = Panel(conteudo, title='Produto', width=34, style='red')
        return etiqta


produto1 = Produto('Caneta', 1.50)
produto2 = Produto('CAMISA OVERSIZED TAM G', price=199.00)
print(produto1.etiqueta())
print(produto2.etiqueta())