# Associação Simples

class Livro:
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor

class Biblioteca: 
    def __init__(self, nome) -> None:
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f'{livro.titulo} - {livro.autor}')

livro1 = Livro('Dom Quixote', 'Miguel de Cervantes')
livro2 = Livro('1984', 'George Orwell')

biblioteca = Biblioteca('Biblioteca Municipal')
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()