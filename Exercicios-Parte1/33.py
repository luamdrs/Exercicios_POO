# Agregação

class Curso:
    def __init__(self, nome, duracao) -> None:
        self.nome = nome
        self.duracao = duracao

class Universidade:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def remover_curso(self, curso):
        self.cursos.remove(curso)    
    
    def listar_cursos(self):
        print(f'Cursos oferecidos pela: {self.nome} ')
        for curso in self.cursos:
            print(f'- {curso.nome} ~ ({curso.duracao}) anos.')

c1 = Curso('Psicologia', 5)
c2 = Curso('Medicina', 6)

universidade = Universidade('Universidade Federal')
universidade.adicionar_curso(c1)
universidade.adicionar_curso(c2)
universidade.listar_cursos()