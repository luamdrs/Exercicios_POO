# Polimorfismo de Substituição + Sobrescrita com super()

class Mae:

    def falar(self):
        return 'A mãe está falando sobre política'


class Pai(Mae):

    def falar(self):
        return 'O pai está falando sobre futebol'


class Filho(Mae):

    def falar(self):
        return 'O filho está falando sobre games'


class Tia(Mae):
    
    def falar(self):
        falar_algo = super().falar()
        return falar_algo + ' e a tia sobre culinária'
    

mae = Mae()
pai = Pai()
filho = Filho()
tia = Tia()

print(mae.falar())
print(pai.falar())
print(filho.falar())
print(tia.falar())