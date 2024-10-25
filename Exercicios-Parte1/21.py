class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


    @property
    def largura(self):
        return self._largura
    
    
    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            raise ValueError('A largura deve ser maior que zero.')
        

    @property
    def altura(self):
        return self._altura
    

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            raise ValueError('A altura deve ser maior que zero.')
        

    @property
    def area(self):
        return self._largura * self._altura
    

    @property
    def perimetro(self):
        return 2 * (self._largura + self._altura)
    

r = Retangulo(5, 3)
print(r.area)
print(r.perimetro)
r.largura = 6
print(r.area)