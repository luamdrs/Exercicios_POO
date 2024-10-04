# Classe Abstrata

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass


class Cachorro(Animal):

    def fazer_som(self):
        return 'O cachorro late.'


class Gato(Animal):

    def fazer_som(self):
        return 'O gato mia.'

# Tentar criar uma instância da classe abstrata gera erro
# animal = Animal()  # Isso não é permitido


# Criando instâncias das subclasses
cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())
print(gato.fazer_som())