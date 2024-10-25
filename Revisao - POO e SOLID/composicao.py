class Endereco:
    def __init__(self, rua, cidade, estado) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
    
    def detalhes(self):
        return f'Rua: {self.rua}, Cidade: {self.cidade} - {self.estado}'


class Pessoa:
    def __init__(self, nome, endereco) -> None:
        self.nome = nome
        self.endereco = endereco
    
    def mostrar_detalhes(self):
        return f'Nome: {self.nome} \nEndereço: {self.endereco.detalhes()}'

endereco = Endereco('13 de Maio', 'São Paulo', 'SP')
pessoa = Pessoa('Ana', endereco)

print(pessoa.mostrar_detalhes())