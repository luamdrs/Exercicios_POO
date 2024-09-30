# __contains__(self, item) -> Permite verificar se um item está contido em um objeto.

class ListaPersonalizada:

    def __init__(self, itens) -> None:
        self.itens = itens

    def __contains__(self, item):
        return item in self.itens


lista = ListaPersonalizada([1, 2, 3, 4])
print(1 in lista)
print(2 in lista)
print(3 in lista)
print(4 in lista)
print(5 in lista) # item não faz parte da lista(objeto)