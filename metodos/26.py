class Pessoa: 
    def __init__(self, nome, idade, senha) -> None:
        self.nome = nome     # Atributo Público
        self._idade = idade  # Atributo Protegido
        self.__senha = senha # Atributo Privado

    # Método para obter o valor da idade (protegido)
    def obter_idade(self):
        return self._idade
    
    # Método para obter a senha (privado)
    def obter_senha(self):
        return self.__senha
    
    # Método para alterar a senha (privado)
    def alterar_senha(self, nova_senha):
        self.__senha = nova_senha


# Criado uma instância da Classe Pessoa
p = Pessoa('Pedro', 21, 'minha_senha_secreta')

# Acessando o atributo público
print(p.nome)

# Acessando o atributo protegido (não recomendado diretamente)
print(p._idade)

# Acessando o atributo privado (não funciona diretamente)
# print(p.__senha) # Gera erro de atributo

# Utilizando métodos para acessar atributos privados
print(p.obter_senha())

# Alterando a senha através de um método
p.alterar_senha('senha123')
print(p.obter_senha())