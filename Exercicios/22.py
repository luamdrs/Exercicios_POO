class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    
    @property
    def saldo(self):
        return self._saldo
    

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError('O saldo não pode ser negativo.')
        
    
    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente.')
        else:
            self._saldo -= valor


conta = ContaBancaria(500)
print(conta.saldo)
conta.sacar(100)
print(conta.saldo)
conta.saldo = 1000
print(conta.saldo)
conta.sacar(1200)