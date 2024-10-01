# Associação Simples

class Departamento:
    def __init__(self, nome) -> None:
        self.nome = nome

class Faculdade:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def remover_departamento(self, departamento):
        self.departamentos.remove(departamento)

    def listar_departamentos(self):
        for departamento in self.departamentos:
            print(departamento.nome)

    def total_departamentos(self):
        return len(self.departamentos)
    
dep1 = Departamento('Ciência da Computação')
dep2 = Departamento('Análise e Desenvolvimento de Sistemas')

faculdade = Faculdade('Faculdade de Tecnologia')

faculdade.adicionar_departamento(dep1)
faculdade.adicionar_departamento(dep2)
faculdade.listar_departamentos()
print(f'Total de departamentos: {faculdade.total_departamentos()}')