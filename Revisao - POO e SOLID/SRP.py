# Representa o usuário
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Valida as informações do usuário
class ValidadorDeUsuario:
    @staticmethod
    def validar_email(email):
        return '@' in email and '.' in email

# Salva o usuário no BD
class RepositorioDeUsuario:
    @staticmethod
    def salvar(usuario):
        print(f'Usuário {usuario.nome} salvo com sucesso no banco de dados.')

# Exibe as info do usuário
class ExibirUsuario:
    @staticmethod
    def exibir(usuario):
        print(f'Nome: {usuario.nome}')
        print(f'Email: {usuario.email}')


usuario = Usuario('Ana', 'ana@email.com', '1234')

if ValidadorDeUsuario.validar_email(usuario.email):
    RepositorioDeUsuario.salvar(usuario)
    ExibirUsuario.exibir(usuario)
else:
    print('Email inválido!')