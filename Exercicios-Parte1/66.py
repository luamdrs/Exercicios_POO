# Herança múltipla -> Uma subclasse pode herdar mais de uma superclasse.

class Animal:

    def mover(self):
        print('Animal se movendo.')


class Ave:

    def voar(self):
        print('Ave voando.')

# Herda de Animal e Ave
class Pato(Animal, Ave):
    pass

pato = Pato()
pato.mover()
pato.voar()