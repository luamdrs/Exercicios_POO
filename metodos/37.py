# Composição

class Comodo:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

class Casa:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.comodos = [Comodo('Sala'), Comodo('Cozinha'), Comodo('Quarto')]

    def mostrar_comodos(self):
        print(f'Casa localizada em {self.endereco} tem os seguintes cômodos: ')
        for comodo in self.comodos:
            print(f'- {comodo.tipo}')

casa = Casa('Rua das Flores, 123')
casa.mostrar_comodos()