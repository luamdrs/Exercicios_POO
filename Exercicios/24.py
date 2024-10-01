class Carro:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade


    @property
    def velocidade(self):
        return self._velocidade
    

    @velocidade.setter
    def velocidade(self, valor):
        if 0 <= valor <= 200:
            self._velocidade = valor
        else:
            raise ValueError('A velocidade deve estar entre 0 e 200.')

carro = Carro()
carro.velocidade = 150
print(carro.velocidade)  
carro.velocidade = 200