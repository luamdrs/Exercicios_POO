class Livro:
    total_livros = 0

    def __init__(self, titulo):
        self.titulo = titulo
        Livro.total_livros += 1

    @classmethod
    def contar_livros(cls):
        return f'Total de livros: {cls.total_livros}'

livro1 = Livro('O Senhor dos Anéis')
livro2 = Livro('1984')
livro3 = Livro('O Pequeno Príncipe')

print(Livro.contar_livros())