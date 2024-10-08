from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def som(self):
        pass


class Gato(Animal):
    def som(self):
        return f'Miau!'


class Cachorro(Animal):
    def som(self):
        return f'Au Au!'


gato = Gato()
cachorro = Cachorro()

print(gato.som())
print(cachorro.som())