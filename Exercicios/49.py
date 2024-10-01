class Personagem:

    def __init__(self, nome, idade, vida) -> None:
        self.nome = nome
        self.idade = idade
        self.vida = vida

    def upgrade_vida(self):
        self.vida += 10

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'


class Mago(Personagem):

    def conjurar_magia(self):
        print(f'{self.nome} lança uma magia aleatória.')

    def upgrade_vida(self):
        self.vida += 5


p1 = Personagem('Zeus', 1000, 1000)
print(p1.nome, p1.idade, p1.vida)

p2 = Personagem('Samus', 30, 100)
print(p2.nome, p2.idade, p2.vida)

p2.upgrade_vida()
print(p2.vida)

print(p2)

p3 = Mago('Gandalf', 1000, 1000)
print(p3)
p3.conjurar_magia()

print(isinstance(p3, Personagem))
print(isinstance(p3, Mago))

p3.upgrade_vida()
print(p3)