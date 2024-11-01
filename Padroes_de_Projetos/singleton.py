class Configuracao:
    _instancia = None

    # Esse método é responsavel por criar uma nova instancia da classe. Ele verifica se ja existe uma instancia. Se nao existir, cria uma.
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
            cls._instancia.config = {} # a config. é armazenada em um dict, permitindo facil acesso e modificaçao.
        return cls._instancia

    def set_config(self, chave, valor):
        self.config[chave] = valor

    def get_config(self, chave):
        return self.config.get(chave)


# Obs: Qualquer parte do código que chamar Configuracao() obterá a mesma instância.

config1 = Configuracao()
config1.set_config('url', 'https://meusite.com')

config2 = Configuracao()
print(config2.get_config('url'))

print(config1 is config2)