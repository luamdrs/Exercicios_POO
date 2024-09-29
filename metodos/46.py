# SOLID (L)

class Ave:
    pass


class AveQueVoa(Ave):

    def voar(self):
        print('Esta ave está voando.')


class Pato(AveQueVoa):

    def voar(self):
        print('O pato está voando!')


class Pinguim(Ave):

    def nadar(self):
        print('O pinguim está nadando.')


ave_que_voa = AveQueVoa()
ave_que_voa.voar()

pato = Pato()
pato.voar()

pinguim = Pinguim()
pinguim.nadar()