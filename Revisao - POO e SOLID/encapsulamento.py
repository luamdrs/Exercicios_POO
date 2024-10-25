class ContaBancaria:
    def __init__(self):
        self.__saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de: R${valor:.2f} realizado com sucesso!')
        else:
            print('Valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print(f'Saque de R${valor:.2f} realizado com sucesso!')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Valor do saque deve ser maior que zero.')

    def mostrar_saldo(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')


conta = ContaBancaria()

conta.depositar(1500)
conta.mostrar_saldo()

conta.sacar(500)
conta.mostrar_saldo()

conta.sacar(1200)
conta.mostrar_saldo()