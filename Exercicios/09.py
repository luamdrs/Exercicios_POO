class Produto:
    lista_produtos = []

    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
        Produto.lista_produtos.append(self)

    @classmethod
    def adicionar_ao_estoque(cls, quantidade):
        for produto in cls.lista_produtos:
            produto.quantidade_em_estoque += quantidade

    def mostrar_estoque(self):
        return f'{self.nome}: {self.quantidade_em_estoque} unidades'
    

p1 = Produto('Teclado', 100, 10)
p2 = Produto('Mouse', 80, 5)

Produto.adicionar_ao_estoque(2)

print(p1.mostrar_estoque())
print(p2.mostrar_estoque())