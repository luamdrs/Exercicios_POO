class Carro:
    # Atributo de classe (pertence à classe e é compartilhado por todas as instâncias)
    quantidade_de_carros = 0

    def __init__(self, marca, modelo):
        # Atributos de instância
        self.marca = marca
        self.modelo = modelo
        Carro.quantidade_de_carros += 1 # Incrementa cada vez que um carro é criado

    # Método de instância
    def mostrar_detalhes(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'
    
    # Método de classe
    @classmethod
    def total_de_carros(cls):
        return f'Total de carros: {cls.quantidade_de_carros}'
    
# Criando instâncias da classe Carro
carro1 = Carro('Toyota', 'Corolla')
carro2 = Carro('Honda', 'Civic')

# Chamando método de instância
print(carro1.mostrar_detalhes())
print(carro2.mostrar_detalhes())

# Chamando um método de classe
print(Carro.total_de_carros())