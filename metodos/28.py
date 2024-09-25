# Associação Simples

class Jogador:
    def __init__(self, nome, posicao) -> None:
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(f'{jogador.nome} - {jogador.posicao}')

j1 = Jogador('Ronaldo', 'Atacante')
j2 = Jogador('Cafu', 'Defensor')

time = Time('Seleção Brasileira')
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.listar_jogadores()