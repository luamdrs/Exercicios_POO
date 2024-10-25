# Getters e Setters controlam o acesso e a modificação dos atributos de uma classe.
# Exemplo sem usar o @property:

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome    # Atributo protegido
        self._idade = idade  # Atributo protegido

    # Getter para 'nome'
    def get_nome(self):
        return self._nome

    # Setter para 'nome'
    def set_nome(self, nome):
        self._nome = nome

    # Getter para 'idade'
    def get_idade(self):
        return self._idade

    # Setter para 'idade'
    def set_idade(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            print('Idade inválida!')


pessoa = Pessoa('Ana', 25)
print(pessoa.get_nome(), pessoa.get_idade())
# Modifica a idade
pessoa.set_idade(30)
print(pessoa.get_idade())