# Polimorfismo de Inclusão 

class Pessoa:

    def falar(self):
        return 'Algo genérico.'


class Menina(Pessoa):
    
    def falar(self):
        return 'A menina está falando algo.'


class Menino(Pessoa):

    def falar(self):
        return 'O menino está falando algo.'


def falar_algo(pessoa: Pessoa):
    print(pessoa.falar())


menina = Menina()
menino = Menino()

falar_algo(menina)
falar_algo(menino)