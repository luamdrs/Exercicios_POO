# __repr__(self) -> A diferença entre __repr__ e __str__ é que 
# __repr__ é voltado para desenvolvedores, enquanto __str__ é voltado para usuários.

class Carro:

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def __repr__(self) -> str:
        return f"Carro(marca= '{self.marca}', modelo= '{self.modelo}')"
    
carro = Carro('Toyota', 'Corolla')
print(repr(carro))