# SOLID (S)
class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class ServicoEmail:

    def enviar_email_boas_vindas(self, usuario):
        print(f"Enviando e-mail de boas-vindas para {usuario.email}.")


class RepositorioUsuario:

    def salvar(self, usuario):
        print(f"Salvando {usuario.nome} no banco de dados.")


# Criando um novo usuário
usuario1 = Usuario('Maria', 'maria@exemplo.com')

# Criando os serviços de email e de banco de dados
servico_email = ServicoEmail()
repositorio_usuario = RepositorioUsuario()

# Enviar o e-mail de boas-vindas
servico_email.enviar_email_boas_vindas(usuario1)

# Salvar o usuário no banco de dados
repositorio_usuario.salvar(usuario1)