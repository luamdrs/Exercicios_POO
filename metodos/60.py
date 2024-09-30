# __iter__(self) ->  Permite que um objeto seja iterado. 
# Necessário para usar o objeto em um loop 'for' ou em expressões de compreensão.

class Contador:
    def __init__(self, limite) -> None:
        self.limite = limite

    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

contador = Contador(10)
for numero in contador:
    print(numero)