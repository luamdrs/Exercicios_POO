'''2. SOLID (O) -> Open/Closed Principle (Princípio Aberto/Fechado)
O código deve estar aberto para extensões, mas fechado para modificações. 
Isso significa que podemos adicionar novas funcionalidades sem alterar o código existente.'''

class Calculadora:

    def calcular(self, operacao):
        return operacao.executar()
    

class Soma:

    def executar(self):
        return 5 + 3
    
calculadora = Calculadora()
print(calculadora.calcular(Soma()))