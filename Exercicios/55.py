# __add__(self, other) -> Pode ser usado para somar 
# objetos de forma personalizada.

class Contador:

    def __init__(self, valor) -> None:
        self.valor = valor

    def __add__(self, outro):
        return Contador(self.valor + outro.valor)
    
    def __str__(self) -> str:
        return str(self.valor)
    

c1 = Contador(10)
c2 = Contador(20)
c3 = c1 + c2
print(c3)