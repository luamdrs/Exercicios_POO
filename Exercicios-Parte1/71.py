# Polimorfismo com Funções

class Retangulo:
    def __init__(self, largura, altura) -> None:
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


class Circulo:
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)


# Função que usa polimorfismo
def imprimir_area(figura):
    print(f'A área da figura é: {figura.area()}')

retangulo = Retangulo(10, 5)
circulo = Circulo(7)

# Usando a mesma função para calcular áreas de diferentes objetos
imprimir_area(retangulo)
imprimir_area(circulo)