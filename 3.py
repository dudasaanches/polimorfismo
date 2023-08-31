class Calculo:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def calcular_valor(self):
        pass

class soma(Calculo):
    def __init__(self,n1, n2):
        super().__init__(n1, n2)

    def calcular_valor(self):
        print(self.n1 + self.n2)

class subtração(Calculo):
    def __init__(self,n1, n2):
        super().__init__(n1, n2)

    def calcular_valor(self):
        print(self.n1 - self.n2)

class multiplicação(Calculo):
    def __init__(self,n1, n2):
        super().__init__(n1, n2)

    def calcular_valor(self):
        print(self.n1 * self.n2)

class divisão(Calculo):
    def __init__(self,n1, n2):
        super().__init__(n1, n2)

    def calcular_valor(self):
       print(self.n1 / self.n2)

n1 = int(input())
n2 = int(input())
somas = [soma(n1,n2), subtração(n1,n2), multiplicação(n1,n2), divisão(n1,n2)]
for i in range(len(somas)):
    somas[i].calcular_valor()