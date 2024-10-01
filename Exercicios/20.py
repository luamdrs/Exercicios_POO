class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @property
    def idade(self):
        return self._idade
    

    @idade.setter
    def idade(self, valor):
        if valor > 0:
            self._idade = valor 
        else:
            raise ValueError('A idade deve ser um valor positivo!')


p1 = Pessoa('Maria', 30)
print(p1.idade)
p1.idade = 28  # Setter define a nova idade
print(p1.idade)