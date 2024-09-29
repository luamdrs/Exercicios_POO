# 4. SOLID (I) -> Interface Segregation Principle (Princípio da Segregação de Interfaces)
# Evite obrigar classes a implementar métodos que não precisam.

class AveQueVoa:

    def voar(self):
        pass


class Pato(AveQueVoa):
    
    def voar(self):
        print('O pato está voando!')


class Pinguim:
    pass


pato = Pato()
pato.voar()