class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}\nE-mail: {self.email}')

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print('Senha alterada com sucesso!')


class SistemaCadastro:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, email, senha):
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        print(f'Usuário {nome} adicionado com sucesso!')

    def exibir_usuarios(self):
        if not self.usuarios:
            print('Nenhum usuário cadastrado.')
        else:
            for usuario in self.usuarios:
                usuario.exibir_informacoes()

    def remover_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                self.usuarios.remove(usuario)
                print(f'Usuário com e-mail {email} removido com sucesso!')
                return
            else:
                print(f'Usuário com e-mail {email} não encontrado.')

usuario1 = Usuario('Vic', 'vic@email.com', '123456')
usuario2 = Usuario('Lua', 'lua@email.com', '456789')

usuario1.exibir_informacoes()
usuario2.exibir_informacoes()

usuario1.alterar_senha('987456')
print(usuario1.senha)

sistema = SistemaCadastro()

sistema.adicionar_usuario('Pedro', 'pedro@email.com', '1256347')
sistema.adicionar_usuario('Alice', 'alice@email.com', '5632147')

sistema.exibir_usuarios()

sistema.remover_usuario('alice@email.com')
sistema.exibir_usuarios()