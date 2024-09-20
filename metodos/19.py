class Carro:
    total_carros = 0

    def __init__(self, modelo, ano, km):
        self.modelo = modelo
        self.ano = ano
        self.km = km
        Carro.total_carros += 1

    # método de instância
    def dirigir(self, km):
        if km > 0:
            self.km += km
            print(f'O carro {self.modelo} agora tem {self.km} km.')
        else:
            print('A km deve ser positiva.')

    
    # método de classe
    @classmethod
    def carros_totais(cls):
        return f'Total de carros criados: {cls.total_carros}'
    

    # método estático
    @staticmethod
    def verificar_km(km):
        if km < 300000:
            return 'Km dentro dos padrões aceitáveis.'
        else:
            return 'Atenção: km alta!'
        

carro1 = Carro('Fusca', 1980, 120000)
carro2 = Carro('Civic', 2015, 45000)

carro1.dirigir(500)
carro2.dirigir(100)

print(Carro.carros_totais())

print(Carro.verificar_km(250000))
print(Carro.verificar_km(300000))