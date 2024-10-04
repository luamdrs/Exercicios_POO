# Composição de Objetos

class Processador:
    def __init__(self, marca, velocidade) -> None:
        self.marca = marca
        self.velocidade = velocidade

    def detalhes(self):
        return f'Processador {self.marca} ~ {self.velocidade}GHz'

class MemoriaRAM:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade

    def detalhes(self):
        return f'Memória RAM de {self.capacidade}GB'


class Disco:
    def __init__(self, tipo, capacidade) -> None:
        self.tipo = tipo
        self.capacidade = capacidade

    def detalhes(self):
        return f'Disco {self.tipo} de {self.capacidade}GB'


class Computador:
    def __init__(self, processador, memoria_ram, disco) -> None:
        self.processador = processador 
        self.memoria_ram = memoria_ram
        self.disco = disco

    def detalhes_completos(self):
        return f'Computador com {self.processador.detalhes()}, {self.memoria_ram.detalhes()} e {self.disco.detalhes()}.'


processador = Processador('Intel', 3.5)
memoria_ram = MemoriaRAM(16)
disco = Disco('SSD', 512)

computador = Computador(processador, memoria_ram, disco)

print(computador.detalhes_completos())