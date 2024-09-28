# SOLID (S): Single Responsibility Principle (Princípio da Responsabilidade Única)
# S: Cada classe deve fazer uma coisa.

class Relatorio:

    def gerar_relatorio(self):
        return 'Relatório Gerado.'
    

class EnviarEmail:

    def enviar(self, mensagem):
        print(f'Enviando email com a mensagem: {mensagem}.')


relatorio = Relatorio()
email = EnviarEmail()

print(relatorio.gerar_relatorio())
email.enviar('Email Recebido. Muito obrigada!')