# Composição

class Quarto:
    def __init__(self, area) -> None:
        self.area = area

    def detalhes(self):
        return f'Quarto de {self.area}m²\n'


class Casa:
    def __init__(self) -> None:
        self.quartos = []

    def adicionar_quarto(self, area):
        quarto = Quarto(area)
        self.quartos.append(quarto)
    
    def detalhes(self):
        detalhes_quartos = ''.join(quarto.detalhes() for quarto in self.quartos)
        return f'Casa com os quartos: \n{detalhes_quartos}'


casa = Casa()
casa.adicionar_quarto(12)
casa.adicionar_quarto(15)

print(casa.detalhes())