# Métodos de Classes
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Criou um método de classe, que não precisa estar disponível em outras instâncias da classe, apenas para a classe em si. Esse método retorna a própria classe, porém com o nome e a idade de acordo com os parâmetros declarados.
    # Retorna um objeto da classe.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


# p1 = Pessoa.por_ano_nascimento('Luana', 1994)
p1 = Pessoa('Luana', 30)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()