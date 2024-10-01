# 5. SOLID (D): Dependency Inversion Principle (Princípio da Inversão de Dependência)
# Dependa de abstrações, não de classes concretas.

class Motor:

    def ligar(self):
        pass


class Carro:
    
    def __init__(self, motor) -> None:
        self.motor = motor

    def dirigir(self):
        self.motor.ligar()


class MotorEletrico(Motor):

    def ligar(self):
        print('Motor elétrico ligado.')


carro = Carro(MotorEletrico())
carro.dirigir()