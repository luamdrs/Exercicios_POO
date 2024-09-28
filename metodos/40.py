'''2. SOLID (O) -> Open/Closed Principle (Princípio Aberto/Fechado)
O código deve estar aberto para extensões, mas fechado para modificações. 
Isso significa que podemos adicionar novas funcionalidades sem alterar o código existente.'''

class Calculadora:

    def calcular(self, operacao):
        return operacao.executar()


class Soma:

    def executar(self):
        return 10 + 2


class Divisao:
    
    def executar(self):
        return 10 / 2


class Subtracao:
    
    def executar(self):
        return 10 - 2


class Multiplicacao:

    def executar(self):
        return 10 * 2


calculadora = Calculadora()
print(calculadora.calcular(Soma()))
print(calculadora.calcular(Divisao()))
print(calculadora.calcular(Subtracao()))
print(calculadora.calcular(Multiplicacao()))