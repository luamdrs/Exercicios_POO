# Composição

class PlacaMae:
    def __init__(self, modelo) -> None:
        self.modelo = modelo

class Computador:
    def __init__(self, marca, modelo_placa) -> None:
        self.marca = marca
        self.placa_mae = PlacaMae(modelo_placa)

    def mostrar_configuracoes(self):
        print(f'Computador: {self.marca}, Placa Mãe: {self.placa_mae.modelo}')

pc = Computador('Dell', 'Intel Z490')
pc.mostrar_configuracoes()