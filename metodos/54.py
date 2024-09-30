# __eq__(self, other) ->  Esse método é usado para comparar 
# dois objetos de forma personalizada.

class Celular:

    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def __eq__(self, outro_celular) -> bool:
        return self.marca == outro_celular.marca and self.modelo == outro_celular.modelo
    

celular1 = Celular('Apple', 'Iphone 16')
celular2 = Celular('Apple', 'Iphone 16')

print(celular1 == celular2)