class Banco:
    total_contas = 0

    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        Banco.total_contas += 1


    @classmethod
    def contas_criadas(cls):
        return f'Total de contas criadas: {cls.total_contas}'
    

conta1 = Banco('Cliente 1')
conta2 = Banco('Cliente 2')
print(Banco.contas_criadas())