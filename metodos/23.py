class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    @property
    def preco(self):
        return self._preco
    

    @preco.setter
    def preco(self, valor):
        if valor >= 1000:
            self._preco = valor * 0.9
        else:
            self._preco = valor


p1 = Produto('Fogão', 1000) # Desconto de 10% aplicado
print(p1.preco)
p1.preco = 950
print(p1.preco) # Sem desconto