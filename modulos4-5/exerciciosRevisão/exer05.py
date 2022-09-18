class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado
    
    def calcula_area(self):
        return self.lado ** 2
    
    def calcula_perimetro(self):
        return self.lado * 4