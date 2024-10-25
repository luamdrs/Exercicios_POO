# Composição

class Motor:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

class Carro:
    def __init__(self, marca, motor_tipo) -> None:
        self.marca = marca
        self.motor = Motor(motor_tipo)

    def mostrar_detalhes(self):
        print(f'Carro: {self.marca}, Motor: {self.motor.tipo}')

carro = Carro('Toyota', 'V8')
carro.mostrar_detalhes()