# SOLID (L) -> Liskov Substitution Principle (Princípio da Substituição de Liskov)
class Animal: 

    def som(self):
        pass


class Cachorro(Animal):
    def som(self):
        return 'Latido'
    

class Gato(Animal):
    def som(self):
        return 'Miau'
    
    
# Funciona para qualquer animal que herde de 'Animal', respeitando o princípio Liskov.
def fazer_barulho(animal):
    print(animal.som())

fazer_barulho(Cachorro())
fazer_barulho(Gato())