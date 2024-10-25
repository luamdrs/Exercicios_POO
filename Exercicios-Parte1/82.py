# Agregação

class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome

    def detalhes(self):
        return f'{self.nome}'


class Escola:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def detalhes(self):
        detalhes_alunos = ''.join(aluno.detalhes() for aluno in self.alunos)
        return f'Escola: {self.nome} \nAlunos: \n{detalhes_alunos}'


aluno1 = Aluno('Maria da Luz')
aluno2 = Aluno('Caio Souza')
aluno3 = Aluno('Ana Júlia')

escola_abc = Escola('Escola ABC')
escola_def = Escola('Escola DEF')
escola_ghi = Escola('Escola GHI')

escola_abc.adicionar_aluno(aluno1)
escola_def.adicionar_aluno(aluno2)
escola_ghi.adicionar_aluno(aluno3)

print(escola_abc.detalhes())
print(escola_def.detalhes())
print(escola_ghi.detalhes())