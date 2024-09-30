# __getitem__(self, key) -> Permite acessar os itens do objeto como
# se ele fosse uma lista ou dicionário.

class Alfabeto:

    def __init__(self) -> None:
        self.letras = ['A', 'B', 'C', 'D']

    def __getitem__(self, index):
        return self.letras[index]
    

alfabeto = Alfabeto()
print(alfabeto[2])