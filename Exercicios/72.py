# Polimorfismo com Duck Typing

class Pato:

    def andar(self):
        return 'O pato está andando.'


class Pessoa:

    def andar(self):
        return 'A pessoa está andando.'


def fazer_andar(objeto):
    print(objeto.andar())


pato = Pato()
pessoa = Pessoa()

fazer_andar(pato)
fazer_andar(pessoa)