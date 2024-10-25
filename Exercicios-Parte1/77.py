# Métodos Abstratos com Argumentos

from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def calcular_area(self, comprimento, largura):
        pass


class Retangulo(Forma):

    def calcular_area(self, comprimento, largura):
        return comprimento * largura


retangulo = Retangulo()
print(retangulo.calcular_area(5, 3))