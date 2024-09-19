from datetime import datetime

class Pessoa:
    ano_atual = datetime.today().year

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de instância
    def apresentar(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'
    
    # Método de classe que funciona como uma fábrica
    @classmethod
    def de_ano_de_nascimento(cls, nome, ano_de_nascimento):
        idade = cls.ano_atual - ano_de_nascimento
        return cls(nome, idade)
    
# Criando uma pessoa pela idade
pessoa1 = Pessoa("João", 30)
print(pessoa1.apresentar()) 

# Criando uma pessoa pelo ano de nascimento
pessoa2 = Pessoa.de_ano_de_nascimento("Maria", 1996)
print(pessoa2.apresentar())  