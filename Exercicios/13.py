class Estacionamento:
    vagas_disponiveis = 100

    def __init__(self, placa):
        self.placa = placa

    
    @classmethod
    def atualizar_vagas(cls, quantidade):
        cls.vagas_disponiveis += quantidade


    def entrar(self):
        if Estacionamento.vagas_disponiveis > 0:
            Estacionamento.atualizar_vagas(-1)
            print(f'Carro {self.placa} entrou. Vagas disponíveis: {Estacionamento.vagas_disponiveis}')
        else:
            print('Estacionamento cheio.')


    def sair(self):
        Estacionamento.atualizar_vagas(1)
        print(f'Carro {self.placa} saiu. Vagas disponíveis: {Estacionamento.vagas_disponiveis}')


carro1 = Estacionamento('ABC-1234')
carro2 = Estacionamento('DFG-5678')

carro1.entrar()
carro2.entrar()
carro1.sair()