# Associação Simples

class Aluno:
    def __init__(self, nome, escola) -> None:
        self.nome = nome
        self.escola = escola

class Escola:
    def __init__(self, nome) -> None:
        self.nome = nome

escola = Escola('Escola ABC')
aluno = Aluno('Pedro', escola)
print(f'O aluno {aluno.nome} estuda na {aluno.escola.nome}.')