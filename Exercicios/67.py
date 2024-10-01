'''
Public -> Público: acessível de qualquer lugar.
Protected -> Protegido: indica que o acesso deve ser feito apenas dentro da classe e subclasses.
Private -> Privado: restrito ao acesso dentro da própria classe, mas acessível com técnicas de mangling.
'''

class Pessoa:
    def __init__(self, nome, idade, senha) -> None:
        self.nome = nome       # Atributo Público
        self._idade = idade    # Atributo Protegido
        self.__senha = senha   # Atributo Privado

    def falar(self):  # Método Público
        print(f'Olá, meu nome é {self.nome}.')

    def aniversario(self):  # Método Protegido
        self._idade += 1

    def __verificar_senha(self, senha):  # Método Privado
        return self.__senha == senha


pessoa = Pessoa('Maria', 18, '1234')
pessoa.falar()
# Acessa diretamente o atributo protegido
print(f'Idade: {pessoa._idade} anos')
# Acessa o atributo privado
print(f'A senha é: {pessoa._Pessoa__senha}')