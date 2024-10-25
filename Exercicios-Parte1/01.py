from random import randint

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    # Método de instância
    # Precisa receber o parâmetro 'self'
    # O 'self' se refere à própria instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


    # Método de Classe
    # Precisa estar decorado com @classmethod 
    # Ele não é referente à instância, mas à classe em si!
    # Ou seja, coisas que forem globais da Classe, é possível criar um class method
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    

    # O Método estático também recebe um decorador
    # Não é utilizado instância 'self' e nem a classe em si 'cls'
    # Pode receber parâmetros se quiser (nome, idade, etc)
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.por_ano_nascimento('Maria', 1994)
p1 = Pessoa('Maria', 30)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# Ambos fazem a mesma coisa.
print(Pessoa.gera_id())
print(p1.gera_id())