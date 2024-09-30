# __call__(self, ...) -> Permite que o objeto seja chamado como uma função.

class Saudacao:

    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    def __call__(self, nome):
        return f'{self.mensagem}, {nome}!'
    

saudacao = Saudacao('Seja bem vindo')
print(saudacao('Pedro'))