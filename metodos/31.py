# Associação Simples

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

class Loja:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def calcular_valor_total(self):
        total = sum(produto.preco for produto in self.produtos)
        return total
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome} - R${produto.preco:.2f}')


p1 = Produto('Notebook', 3500)
p2 = Produto('Mouse', 150)
p3 = Produto('Teclado Mecânico', 300)
p4 = Produto('Mousepad', 100)

loja = Loja('Loja de Eletrônicos')
loja.adicionar_produto(p1)
loja.adicionar_produto(p2)
loja.adicionar_produto(p3)
loja.adicionar_produto(p4)
loja.remover_produto(p3)
loja.listar_produtos()
print(f'Valor total: R${loja.calcular_valor_total():.2f}')