# __getitem__(self, key) e __setitem__(self, key, value) -> Permitem o uso da notação de 
# colchetes para acessar (`__getitem__`) e modificar (`__setitem__`) itens do objeto.

class DicionarioPersonalizado:
    def __init__(self) -> None:
        self.dados = {}

    def __getitem__(self, chave):
        return self.dados[chave]
    
    def __setitem__(self, chave, valor):
        self.dados[chave] = valor

dicionario = DicionarioPersonalizado()
dicionario['Py'] = 'Python'
print(dicionario['Py'])
dicionario['Py'] = 'Python for everybody!'
print(dicionario['Py'])