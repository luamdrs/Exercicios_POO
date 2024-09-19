class Animal:
    # Atributo de Classe
    quantidade_animais = 0
    
    def __init__(self, nome):
        self.nome = nome
        Animal.quantidade_animais += 1  # Incrementa o contador a cada criação

    # Método de instância 
    def falar(self):
        return f'{self.nome} está fazendo um som!'
    
    # Método de classe para mostrar quantos animais foram criados
    @classmethod
    def contar_animais(cls):
        return f'Total de animais: {cls.quantidade_animais}'
    
# Criando instâncias
gato = Animal('Gato')
cachorro = Animal('Cachorro')

# Método de instância
print(gato.falar())
print(cachorro.falar())

# Método de Classe
print(Animal.contar_animais())