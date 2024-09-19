class FormaGeometrica:
    def calcular_area(self):
        raise NotImplementedError('Este método deve ser sobrescrito.')


    @classmethod
    def fazer_forma(cls, tipo, *args):
        if tipo == 'retangulo':
            return Retangulo(*args)
        elif tipo == 'circulo': 
            return Circulo(*args)
        else:
            raise ValueError('Tipo de forma desconhecido!')
        
    
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)
    

retangulo = FormaGeometrica.fazer_forma('retangulo', 4, 5)
circulo = FormaGeometrica.fazer_forma('circulo', 3)

print(f'Área do Retângulo: {retangulo.calcular_area()}')
print(f'Área do Círculo: {circulo.calcular_area()}')