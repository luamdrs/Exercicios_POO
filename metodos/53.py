# __len__(self) -> Define o comportamento da função len() quando aplicada ao objeto.

class ListaPersonalizada:

    def __init__(self, itens) -> None:
        self.itens = itens

    def __len__(self):
        return len(self.itens)
    
lista = ListaPersonalizada([1, 2, 3, 4, 5])
print(len(lista))