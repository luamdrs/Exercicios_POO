# Herança -> SuperClasse e SubClasse -> Em Python, uma classe herda de outra passando 
# o nome da superclasse entre parênteses ao definir a subclasse.

class Animal: # SuperClasse
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} está fazendo um som.')


class Gato(Animal): # SubClasse
    
    def emitir_som(self):
        print(f'{self.nome} está miando.')


class Cachorro(Animal): # SubClasse

    def emitir_som(self):
        print(f'{self.nome} está latindo.')


cavalo = Animal('Cavalo')
cavalo.emitir_som()

gato = Gato('Amy')
gato.emitir_som()

cachorro = Cachorro('Suzi')
cachorro.emitir_som()