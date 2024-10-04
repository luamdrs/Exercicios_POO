# Uso do super() com Métodos Abstratos

from abc import ABC, abstractmethod

class Veiculo(ABC):

    def iniciar(self):
        print('O veículo está ligado.')

    @abstractmethod
    def dirigir(self):
        pass


class Carro(Veiculo):

    def dirigir(self):
        print('Dirigindo um carro.')
    

carro = Carro()
carro.iniciar()
carro.dirigir()