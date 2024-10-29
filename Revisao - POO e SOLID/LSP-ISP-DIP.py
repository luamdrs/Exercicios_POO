from abc import ABC, abstractmethod

class Reproduzivel(ABC):
    @abstractmethod
    def reproduzir(self):
        pass

class Legivel(ABC):
    @abstractmethod
    def ler(self):
        pass

class RepositorioDeMidia(ABC):
    @abstractmethod
    def salvar(self, midia):
        pass

class Midia(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

class Ebook(Midia, Legivel):
    def __init__(self, titulo, numero_paginas):
        super().__init__(titulo)
        self.numero_paginas = numero_paginas

    def ler(self):
        print(f'Exibindo o e-book: {self.titulo} com {self.numero_paginas} páginas.')

class Audiolivro(Midia, Reproduzivel):
    def __init__(self, titulo, duracao):
        super().__init__(titulo)
        self.duracao = duracao

    def reproduzir(self):
        print(f'Tocando o audiolivro: {self.titulo} (Audiobook) com duração de {self.duracao} horas.')

class RepositorioBancoDeDados(RepositorioDeMidia):
    def salvar(self, midia):
        print(f'Salvando {midia.titulo} no banco de dados.')

class RepositorioDeArquivoJson(RepositorioDeMidia):
    def salvar(self, midia):
        print(f'Salvando {midia.titulo} em um arquivo JSON.')

class GestorDeMidias:
    def __init__(self, repositorio: RepositorioDeMidia):
        self.repositorio = repositorio

    def salvar_midia(self, midia: Midia):
        self.repositorio.salvar(midia)

    def executar_midia(self, midia: Midia):
        if isinstance(midia, Reproduzivel):
            midia.reproduzir()
        elif isinstance(midia, Legivel):
            midia.ler()

ebook = Ebook('A Arte da Guerra', 200)
audiolivro = Audiolivro('A Arte da Guerra', 5)

repositorio_bd = RepositorioBancoDeDados()
gestor_midias_bd = GestorDeMidias(repositorio_bd)

repositorio_json = RepositorioDeArquivoJson()
gestor_midias_json = GestorDeMidias(repositorio_json)

gestor_midias_bd.salvar_midia(ebook)
gestor_midias_bd.executar_midia(ebook)

gestor_midias_json.salvar_midia(audiolivro)
gestor_midias_json.executar_midia(audiolivro)