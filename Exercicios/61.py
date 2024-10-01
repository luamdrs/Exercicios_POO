# __hash__(self) -> Define o valor de hash do objeto. 
# Usado em estruturas de dados como set e dict.

class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


ponto1 = Ponto(1, 2)
ponto2 = Ponto(1, 2)
ponto3 = Ponto(1, 2)

# Todos serão tratados como o mesmo ponto
conjunto = {ponto1, ponto2, ponto3}
print(len(conjunto))