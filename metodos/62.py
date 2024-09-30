# __bool__(self) -> Define o valor booleano do objeto, 
# usado em contextos que requerem uma avaliação de verdade (como `if` ou `while`).

class Lista:
    def __init__(self, itens) -> None:
        self.itens = itens

    def __bool__(self):
        return len(self.itens) > 0
    
lista_vazia = Lista([])
lista_com_itens = Lista([10, 20, 30, 40])

print(bool(lista_vazia))
print(bool(lista_com_itens))