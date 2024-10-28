class Midia:
    def __init__(self, titulo):
        self.titulo = titulo

    def reproduzir(self):
        raise NotImplementedError('Este método deve ser implementado pelas subclasses.')

class Ebook(Midia):
    def __init__(self, titulo, numero_paginas):
        super().__init__(titulo)
        self.numero_paginas = numero_paginas

    def reproduzir(self):
        print(f'Exibindo o e-book: {self.titulo} com {self.numero_paginas} páginas.')

class Audiolivro(Midia):
    def __init__(self, titulo, duracao):
        super().__init__(titulo)
        self.duracao = duracao

    def reproduzir(self):
        print(f'Tocando o audiolivro: {self.titulo} (Audiobook) com duração de {self.duracao} horas.')

def executar_midia(midia):
    midia.reproduzir()


ebook = Ebook('A Arte da Guerra', 200)
audiolivro = Audiolivro('A Arte da Guerra', 5)

executar_midia(ebook)
executar_midia(audiolivro)