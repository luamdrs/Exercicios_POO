class Veiculo:
    def __init__(self, marca) -> None:
        self.marca = marca

    def mover(self):
        print('O veículo está se movendo.')


class Automovel:
    def __init__(self, combustivel) -> None:
        self.combustivel = combustivel

    def abastecer(self):
        print('O automóvel foi abastecido.')


class Moto(Veiculo, Automovel):
    def __init__(self, marca, combustivel, cilindradas) -> None:
        Veiculo.__init__(self, marca)
        Automovel.__init__(self, combustivel)
        self.cilindradas = cilindradas

    def detalhes(self):
        return f'Marca: {self.marca}, Combustível: {self.combustivel}, Cilindradas: {self.cilindradas}'


moto = Moto('Yamaha', 'Gasolina', 500)

moto.mover()
moto.abastecer()

print(moto.detalhes())