class Configuracao:
    # Atributo de Classe
    modo_debug = False

    # Método de instância
    def mostrar_config(self):
        return f'Modo debug está {'ativado' if Configuracao.modo_debug else 'desativado'}'
    
    # Método de classe para alterar a configuração
    @classmethod
    def ativar_debug(cls):
        cls.modo_debug = True

    @classmethod
    def desativar_debug(cls):
        cls.modo_debug = False

# Criando uma instância
config = Configuracao()

# Verificando o modo debug
print(config.mostrar_config())

# Ativando o modo debug
Configuracao.ativar_debug()

# Verificar novamente
print(config.mostrar_config())