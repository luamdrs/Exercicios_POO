# Agregação

class Autor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

class Livraria:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.autores = []

    def cadastrar_autor(self, autor):
        self.autores.append(autor)

    def listar_autores(self):
        print(f'Autores disponíveis na {self.nome}')
        for autor in self.autores:
            print(f'- {autor.nome} ~ Livros: {', '.join(autor.livros)}')

autor1 = Autor('J.K. Rowling')
autor1.adicionar_livro('Harry Potter e a Pedra Filosofal')
autor1.adicionar_livro('Harry Potter e a Câmara Secreta')

livraria = Livraria('Livraria Central')
livraria.cadastrar_autor(autor1)
livraria.listar_autores()