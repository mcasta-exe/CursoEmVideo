from rich import print
from rich import inspect

class Funcionario:
    #ATRIBUTOS DE CLASSE
    empresa = "MAT RECORDS"

    #ATRIBUTOS DE INSTÂNCIA
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    #MÉTODOS
    def apresentar(self):
        return (f" Meu nome é [blue]{self.nome}[/], sou {self.cargo} do setor de {self.setor} :computer:"
                f" da empresa {Funcionario.empresa}")


Funcionario.empresa="CASTECH" #ALTERADO A EMPRESA ATRIBUTO DA CLASSE APENAS AQUI.
p1 = Funcionario('Matheus', 'T.I', 'Dev. Júnior')
print(p1.apresentar())
#inspect(p1, methods=True)


