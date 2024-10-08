class Calculadora:
    @classmethod
    def somar(cls, x, y):
        return x + y

    @staticmethod
    def subtrair(x, y):
        return x - y

calculadora = Calculadora()

print(f'Soma: {calculadora.somar(5, 2)}')
print(f'Subtração: {calculadora.subtrair(5, 2)}')
