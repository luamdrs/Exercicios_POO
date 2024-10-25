# Polimorfismo com Herança

class Animal:
    
    def falar(self):
        pass   # Método genérico que será sobrescrito


class Cachorro:

    def falar(self):
        return 'O cachorro late.'


class Gato:

    def falar(self):
        return 'O gato mia.'


animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())
