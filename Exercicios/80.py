# Agregação de objetos

class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome

    def detalhes(self):
        return f'\n{self.nome}'


class Curso:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.alunos = [] # Agregação: o Curso pode ter vários Alunos

    def adicionar_alunos(self, aluno):
        self.alunos.append(aluno)

    def detalhes(self):
        detalhes_alunos = ''.join(aluno.detalhes() for aluno in self.alunos)
        return f'Curso: {self.nome} \nAlunos: {detalhes_alunos}'


aluno1 = Aluno('Pedro da Silva')
aluno2 = Aluno('Ana Maria')

curso_engenharia = Curso('Engenharia de Software')
curso_engenharia.adicionar_alunos(aluno1)
curso_engenharia.adicionar_alunos(aluno2)

print(curso_engenharia.detalhes())