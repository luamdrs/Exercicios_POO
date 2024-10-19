import math

class FormaGeometrica:
    def area(self):
        raise NotImplementedError('Este método deve ser implementado por subclasses.')


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

circulo = Circulo(5)
quadrado = Quadrado(4)

print(f'Área do círculo: {circulo.area():.2f}')
print(f'Área do quadrado: {quadrado.area():.2f}')