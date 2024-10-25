class Calculadora:
    @staticmethod
    def multiplicar(a, b):
        multip = a * b
        print(f'O valor da multiplicação é: {multip} ')
        return multip
    

    @staticmethod
    def divisao(a, b):
        try: 
            divis = a / b
            print(f'O valor da divisão é: {divis}')
            return divis
        except ZeroDivisionError:
            print('Não é possível dividir por zero.')
            return None



resultado_multiplicacao = Calculadora.multiplicar(5, 6)
resultado_divisao1 = Calculadora.divisao(5, 0)
resultado_divisao2 = Calculadora.divisao(6, 2)