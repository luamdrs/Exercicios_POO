class Circulo:
    # Atributo de Classe
    pi = 3.14

    def __init__(self, raio):
        self.raio = raio

    # Método de instância
    def calcular_area(self):
        return Circulo.pi * (self.raio ** 2)
    
    # Método de classe para alterar o valor de pi
    @classmethod
    def alterar_pi(cls, novo_pi):
        cls.pi = novo_pi

# Criando instâncias de círculo
circulo1 = Circulo(5)
print(circulo1.calcular_area())

# Alterando o valor de pi usando um método de classe
Circulo.alterar_pi(3.14159)

# Calculando a área novamente com o novo valor de pi
circulo2 = Circulo(5)
print(circulo2.calcular_area())