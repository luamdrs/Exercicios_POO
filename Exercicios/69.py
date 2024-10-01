# Usando @property para Getters e Setters

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    # Getter para 'nome' usando @property
    @property
    def nome(self):
        return self._nome
    
    # Setter para 'nome'
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Getter para 'idade'
    @property
    def idade(self):
        return self._idade
    
    # Setter para 'idade' com validação
    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            print('Idade inválida.')


pessoa = Pessoa('Pedro', 15)
# Acessa o nome como se fosse um atributo, mas usa o getter
print(pessoa.nome, pessoa.idade)
# Modifica a idade usando o setter
pessoa.idade = 18
print(pessoa.idade)