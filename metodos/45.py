# SOLID (O)
class MetodoPagamento:

    def processar(self):
        raise NotImplementedError('Este método deve ser implementado por subclasses.')
    

class Paypal(MetodoPagamento):

    def processar(self):
        print('Processando pagamento com PayPal.')


class Pix(MetodoPagamento):

    def processar(self):
        print('Processando pagamento com Pix.')


class CartaoDeCredito(MetodoPagamento):
    
    def processar(self):
        print('Processando pagamento com Cartão de Crédito.')


class ProcessadorPagamento:

    def processar(self, metodo_pagamento: MetodoPagamento):
        metodo_pagamento.processar()


paypal = Paypal()
paypal.processar()

pix = Pix()
pix.processar()

carta_de_credito = CartaoDeCredito()
carta_de_credito.processar()