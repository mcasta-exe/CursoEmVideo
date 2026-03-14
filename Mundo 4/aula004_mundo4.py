#Declaração de classe
class Gafanhoto:
    # Atributos de instancia
    def __init__(self):
        self.nome = ''
        self.idade = 0
    # Métodos de instancia
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f"O {self.nome} tem {self.idade} anos"


#Programa principal

g1=Gafanhoto()
g1.nome = 'João'
g1.idade = 28
g1.aniversario()
print(g1.mensagem())