class Funcionario:
    funcionarios = []

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Funcionario.funcionarios.append(self)


    @classmethod
    def aumentar_salario(cls, porcentagem):
        for funcionario in cls.funcionarios:
            funcionario.salario += funcionario.salario * (porcentagem / 100)


    def mostrar_salario(self):
        return f'{self.nome} tem salário de R${self.salario:.2f}'
    

f1 = Funcionario('Ana', 2000)
f2 = Funcionario('João', 3500)

Funcionario.aumentar_salario(10)

print(f1.mostrar_salario())
print(f2.mostrar_salario())