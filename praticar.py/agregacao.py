class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def detalhes(self):
        return f'Produto: {self.nome}, Preço: R${self.preco:.2f}'


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_valor_total(self):
        total = sum([produto.preco for produto in self.produtos])
        return total

    def exibir_produtos(self):
        for produto in self.produtos:
            print(produto.detalhes())


produto1 = Produto('Arroz', 4.50)
produto2 = Produto('Feijão', 6.80)
produto3 = Produto('Macarrão', 2.60)
produto4 = Produto('Café', 9.99)

carrinho = CarrinhoDeCompras()

carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)
carrinho.adicionar_produto(produto4)

carrinho.exibir_produtos()
print(f'Valor total: R${carrinho.calcular_valor_total():.2f}')