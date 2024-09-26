# Agregação

class Funcionario:
    def __init__(self, nome, cargo) -> None:
        self.nome = nome
        self.cargo = cargo

class Empresa:
    def __init__(self, nome) -> None:
        self.nome = nome 
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def demitir_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def listar_funcionarios(self):
        print(f'Funcionários da {self.nome}: ')
        for funcionario in self.funcionarios:
            print(f'- {funcionario.nome}, {funcionario.cargo}')

f1 = Funcionario('Ana', 'Engenharia')
f2 = Funcionario('Pedro', 'Desenvolvedor')

empresa = Empresa('TechCorp')
empresa.contratar_funcionario(f1)
empresa.contratar_funcionario(f2)
empresa.listar_funcionarios()