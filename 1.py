class AnimalAquatico:
    def Acao(self):
       return "Nadando"

class Peixe(AnimalAquatico):
    def Acao(self):
        print(super(). Acao(),"no Rio")

class Tartaruga(AnimalAquatico):
    def Acao(self):
        print(super(). Acao(),"no Mar")

Animal= Peixe()
Animal.Acao()
Animal= Tartaruga()
Animal.Acao()