# SOLID (D)

class Dispositivo:

    def ligar(self):
        pass


class Televisao(Dispositivo):

    def ligar(self):
        print('A TV está ligada.')


class ControleRemoto:

    def __init__(self, dispositivo: Dispositivo) -> None:
        self.dispositivo = dispositivo

    def ligar(self):
        self.dispositivo.ligar()


# Instanciando uma TV
tv = Televisao()
# Associando a TV ao controle remoto
controle = ControleRemoto(tv)
# Ligando a TV através do controle remoto
controle.ligar()