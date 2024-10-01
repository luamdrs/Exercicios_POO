# Se você quiser acessar o comportamento 
# da superclasse dentro da subclasse, pode usar a função super().

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        print(f'{self.nome} está fazendo um som.')


class Cachorro(Animal):
    def __init__(self, nome, raca) -> None:
        super().__init__(nome)  # Chama o __init__ da superclasse
        self.raca = raca

    def emitir_som(self):
        super().emitir_som()  # Chama o método da superclasse
        print(f'{self.nome} está latindo.')

# Criando um objeto Cachorro
cachorro = Cachorro('Rex', 'Labrador')
cachorro.emitir_som()