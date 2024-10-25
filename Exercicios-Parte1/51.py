# Polimorfismo

# A class Criatura é o pai das classes Orc e Minotauro
class Criatura:

    def __init__(self, nome) -> None:
        self.nome = nome    

    def informacao(self):
        raise NotImplementedError('Subclasse deve Implementar o Método Abstrato.')


class Orc(Criatura):

    def informacao(self):
        return 'Criatura tribal shamânica misteriosa.'


class Minotauro(Criatura):

    def informacao(self):
        return 'Criatura poderosa que vive nos labirintos.'


criaturas = [Orc('Orc 1'), Orc('Orc 2'), Minotauro('Minotauro')]
for criatura in criaturas:
    print(f'Nome: {criatura.nome}, Informações: {criatura.informacao()}')