class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Método de instância
    def calcular_area(self):
        return self.base * self.altura
    
    # Método de instância
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    

ret = Retangulo(5, 3)
print(ret.calcular_area())
print(ret.calcular_perimetro())