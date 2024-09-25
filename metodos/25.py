# Atributos de Classe

class Carro:
    rodas = 4 # Atributo de Classe

    def __init__(self, marca) -> None:
        self.marca = marca # Atributo de instância


# Criando dois objetos (instâncias) da Classe Carro
carro1 = Carro('Toyota')
carro2 = Carro('Honda')

# Acessando atributo de Classe
print(carro1.rodas)
print(carro2.rodas)

# Modificando atributo de Classe através da Classe
Carro.rodas = 6

# Todos os objetos refletem a mundança
print(carro1.rodas)
print(carro2.rodas)

# Mudança em uma instância:
# Cria um atributo de instância específico para carro1
carro1.rodas = 8

# A instância carro1 irá receber um valor diferente
print(carro1.rodas)
# Enquanto a instância carro2 permanece com o mesmo valor
print(carro2.rodas)