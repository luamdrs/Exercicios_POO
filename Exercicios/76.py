# Classe Abstrata com Atributos e Métodos Normais

from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, cor) -> None:
        self.cor = cor

    def mostrar_cor(self):
        return f'A cor da forma é {self.cor}'

    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)


circulo = Circulo('vermelho', 5)
print(circulo.mostrar_cor())
print(circulo.calcular_area())