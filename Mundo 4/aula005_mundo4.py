#Declaração de classe
class Gafanhoto:
    # Atributos de instancia
    def __init__(self,nome='<desconhecido>',idade=0):
        self.nome = nome
        self.idade = idade
    # Métodos de instancia
    def aniversario(self):
        self.idade += 1
    def __str__(self): #Substitui o metodo mensagem. Sem necessidade de atribuir a função (.mensagem())
        return f"O {self.nome} tem {self.idade} anos"
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; Idade = {self.idade}"

    
#Programa principal(Declaração de Objetos)

g1=Gafanhoto("João", 28)
g1.aniversario()
print(g1)
print(g1.__dict__) #Atributo. Similar ao getstate
print(g1.__getstate__()) #Metodo personalizável


g2 = Gafanhoto()
print(g2)