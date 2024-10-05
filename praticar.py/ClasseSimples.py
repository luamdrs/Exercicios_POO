class Cachorro:
    def __init__(self, nome, idade, raca) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print('O cachorro está latindo.')

    def detalhes(self):
        return f'Nome: {self.nome} \nIdade: {self.idade} \nRaça: {self.raca}'
    
cachorro = Cachorro('Bel', 2, 'Golden Retriever')
cachorro.latir()
print(cachorro.detalhes())