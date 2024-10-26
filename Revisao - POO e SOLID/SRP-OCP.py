class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Validações
class ValidadorDeUsuario:
    @staticmethod
    def validar_email(email):
        return '@' in email and '.' in email

class ValidadorDeSenha:
    def validar(self, senha):
        raise NotImplementedError('Este método deve ser implementado pelas subclasses.')

class ValidadorComprimentoSenha(ValidadorDeSenha):
    def validar(self, senha):
        return len(senha) > 8

class ValidadorCaracteresEspeciais(ValidadorDeSenha):
    def validar(self, senha):
        especiais = "!@#$%^&*()-_=+"
        return any(char in especiais for char in senha)

# Repositórios
class RepositorioUsuario:
    def salvar(self, usuario):
        raise NotImplementedError('Este método deve ser implementado pelas subclasses.')

class RepositorioBancoDeDados(RepositorioUsuario):
    def salvar(self, usuario):
        print(f'Usuário {usuario.nome} salvo no banco de dados.')

class RepositorioArquivoJson(RepositorioUsuario):
    def salvar(self, usuario):
        print(f'Usuário {usuario.nome} salvo em arquivo JSON.')

# Exibição
class ExibirUsuario:
    @staticmethod
    def exibir(usuario):
        print(f'Nome: {usuario.nome}')
        print(f'Email: {usuario.email}')

def cadastrar_usuario(usuario, validadores_senha, repositorio):
    if not ValidadorDeUsuario.validar_email(usuario.email):
        print('Email inválido.')
        return

    for validador in validadores_senha:
        if not validador.validar(usuario.senha):
            print('Senha inválida.')
            return

    repositorio.salvar(usuario)
    print('Usuário cadastrado com sucesso!')


usuario = Usuario('Ana', 'ana@email.com', 'senha@123')
validador1 = ValidadorComprimentoSenha()
validador2 = ValidadorCaracteresEspeciais()
repositorio_bd = RepositorioBancoDeDados()

cadastrar_usuario(usuario, [validador1, validador2], repositorio_bd)

repositorio_json = RepositorioArquivoJson()

cadastrar_usuario(usuario, [validador1, validador2], repositorio_json)