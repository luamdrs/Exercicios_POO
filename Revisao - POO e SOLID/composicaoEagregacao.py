class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0


class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def media_geral(self):
        total_media  = 0
        for aluno in self.alunos:
            total_media += aluno.media()
        if self.alunos:
            return total_media / len(self.alunos)
        return 0


curso = Curso('Matemática')
aluno1 = Aluno('João')
aluno2 = Aluno('Maria')
aluno3 = Aluno('Pedro')

curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)
curso.adicionar_aluno(aluno3)

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7.5)
aluno2.adicionar_nota(9)
aluno2.adicionar_nota(9.8)
aluno3.adicionar_nota(10)
aluno3.adicionar_nota(8.5)

print(f'Média de {aluno1.nome}: {aluno1.media():.2f}')
print(f'Média de {aluno2.nome}: {aluno2.media():.2f}')
print(f'Média de {aluno3.nome}: {aluno3.media():.2f}')
print(f'Média Geral do Curso: {curso.media_geral():.2f}')