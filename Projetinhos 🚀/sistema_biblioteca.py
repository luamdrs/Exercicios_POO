class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print(f'Título: {self.titulo}\nAutor: {self.autor}')


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def pegar_emprestado(self, livro, biblioteca):
        if livro in biblioteca.livros_disponiveis:
            self.livros_emprestados.append(livro)
            biblioteca.emprestar_livro(livro, self)
            print(f'{self.nome} pegou o livro "{livro.titulo}" emprestado.')
        else:
            print(f'O livro {livro.titulo} não está disponível no momento.')

    def devolver_livro(self, livro, biblioteca):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            biblioteca.receber_devolucao(livro, self)
            print(f'{self.nome} devolveu o livro "{livro.titulo}".')
        else:
            print(f'{self.nome} não possui o livro "{livro.titulo}."')

    def exibir_livros_emprestados(self):
        if not self.livros_emprestados:
            print(f'{self.nome} não possui nenhum livro emprestado.')
        else:
            print(f'Livros emprestados por {self.nome}:')
            for livro in self.livros_emprestados:
                livro.exibir_detalhes()


class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = []
        self.livros_emprestados = []

    def adicionar_livro(self, livro):
        self.livros_disponiveis.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca!')

    def emprestar_livro(self, livro, usuario):
        self.livros_disponiveis.remove(livro)
        self.livros_emprestados.append(livro)

    def receber_devolucao(self, livro, usuario):
        self.livros_emprestados.remove(livro)
        self.livros_disponiveis.append(livro)

    def exibir_livros_disponiveis(self):
        if not self.livros_disponiveis:
            print('Nenhum livro disponível na biblioteca.')
        else:
            print('Livros disponíveis na biblioteca:')
            for livro in self.livros_disponiveis:
                livro.exibir_detalhes()


biblioteca = Biblioteca()
livro1 = Livro('Morte no Nilo', 'Agatha Christie')
livro2 = Livro('Os Fornos de Hitler', 'Olga Lengyel')
livro3 = Livro('O Homem de Giz', 'C.J Tudor')
livro4 = Livro('Noite sem fim', 'Agatha Christie')

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)

usuario1 = Usuario('Pedro')
usuario2 = Usuario('Júlia')

usuario1.pegar_emprestado(livro2, biblioteca)
usuario2.pegar_emprestado(livro1, biblioteca)

biblioteca.exibir_livros_disponiveis()

usuario1.devolver_livro(livro2, biblioteca)
usuario2.devolver_livro(livro1, biblioteca)

biblioteca.exibir_livros_disponiveis()