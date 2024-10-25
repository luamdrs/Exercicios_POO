class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print(f'{self.nome} está falando.')


class Professor(Pessoa):
    def falar(self):
        print(f'O Professor {self.nome} está falando.')
    
    def ensinar(self, disciplina):
        print(f'O Professor {self.nome} está ensinando {disciplina}.')


pessoa = Pessoa('Ana', 22)
pessoa.falar()

professor = Professor('Paulo', 40)
professor.falar()
professor.ensinar('Estatística')
