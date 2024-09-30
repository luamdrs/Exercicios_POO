# Encapsulamento

class Objeto(object):

    def __init__(self) -> None:
        self.x = 1    # Permitido o acesso direto
        self._x = 1   # Deve ser considerado privado
        self.__x = 1  # Considerado privado


obj = Objeto()
print(obj.x)
print(obj._x)
# print(obj.__x)  # Nos é retornado um erro. Para podermos
# acessá-lo é necessário chamarmos ele através do Objeto diretamente:
print(obj._Objeto__x)