# SOLID (I)

class AveQueVoa:

    def voar(self):
        pass


class AveQueNada:

    def nadar(self):
        pass


class Pato(AveQueVoa, AveQueNada):

    def voar(self):
        print('O pato está voando!')

    def nadar(self):
        print('O pato está nadando!')


class Pinguim(AveQueNada):

    def nadar(self):
        print('O pinguim está nadando!')


pato = Pato()
pato.voar()
pato.nadar()

pinguim = Pinguim()
pinguim.nadar()