class Pagina:
    def __init__(self, numero, conteudo) -> None:
        self.numero = numero
        self.conteudo = conteudo

class Livro:
    def __init__(self, titulo) -> None:
        self.titulo = titulo
        self.paginas = []

    def adicionar_pagina(self, numero, conteudo):
        self.paginas.append(Pagina(numero, conteudo))

    def mostrar_paginas(self):
        print(f'Livro: {self.titulo}')
        for pagina in self.paginas:
            print(f'Página {pagina.numero}: {pagina.conteudo[:30]}...')

livro = Livro('Python para Iniciantes')
livro.adicionar_pagina(1, 'Introdução à programação.')
livro.adicionar_pagina(2, 'Variáveis, tipos e operadores.')
livro.adicionar_pagina(3, 'Estruturas de decisação.')
livro.adicionar_pagina(4, 'Estruturas de repeticão.')
livro.mostrar_paginas()