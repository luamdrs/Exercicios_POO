class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True
        print(f'Tarefa "{self.titulo}" marcada como concluída.')

    def exibir_detalhes(self):
        print(f'Tarefa: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.concluida}')


class ListaDeTarefas:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa.titulo}" adicionada à lista "{self.nome}".')

    def remover_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                self.tarefas.remove(tarefa)
                print(f'Tarefa "{titulo}" removida da lista "{self.nome}".')
                return
        print(f'Tarefa "{titulo}" não encontrada na lista "{self.nome}".')

    def exibir_tarefas(self):
        if not self.tarefas:
            print(f'Não há tarefas na lista "{self.nome}".')
        else:
            print(f'Tarefas da lista "{self.nome}":')
            for tarefa in self.tarefas:
                tarefa.exibir_detalhes()

    def exibir_tarefas_concluidas(self):
        tarefas_concluidas = [tarefa for tarefa in self.tarefas if tarefa.concluida]    
        if not tarefas_concluidas:
            print(f'Não há tarefas concluídas na lista "{self.nome}".')
        else:
            print(f'Tarefas concluídas na lista "{self.nome}":')
            for tarefa in tarefas_concluidas:
                tarefa.exibir_detalhes()    


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.listas = []

    def criar_lista(self, nome):
        nova_lista = ListaDeTarefas(nome)
        self.listas.append(nova_lista)
        print(f'Lista "{nome}" criada.')

    def exibir_listas(self):
        if not self.listas:
            print(f'"{self.nome}" não possui listas de tarefas.')
        else:
            print(f'Lista de tarefas de "{self.nome}":')
            for lista in self.listas:
                print(f'- {lista.nome}')

    def adicionar_tarefa_a_lista(self, nome_lista, tarefa):
        for lista in self.listas:
            if lista.nome == nome_lista:
                lista.adicionar_tarefa(tarefa)
                return
        print(f'Lista "{nome_lista}" não encontrada.')

    def remover_tarefa_de_lista(self, nome_lista, titulo_tarefa):
        for lista in self.listas:
            if lista.nome == nome_lista:
                lista.remover_tarefa(titulo_tarefa)
                return
        print(f'Lista "{nome_lista}" não encontrada.')


usuario = Usuario('Laura')

usuario.criar_lista('Estudos')
usuario.criar_lista('Trabalho')
usuario.criar_lista('Pessoal')

tarefa1 = Tarefa('Projeto', 'Finalizar o projeto.')
tarefa2 = Tarefa('Relatório', 'Completar o relatório semanal')
tarefa3 = Tarefa('Livro', 'Finalizar o livro Morte no Nilo')

usuario.adicionar_tarefa_a_lista('Estudos', tarefa1)
usuario.adicionar_tarefa_a_lista('Trabalho', tarefa2)
usuario.adicionar_tarefa_a_lista('Pessoal', tarefa3)

usuario.exibir_listas()

usuario.listas[0].exibir_tarefas()
tarefa1.marcar_concluida()

usuario.listas[0].exibir_tarefas_concluidas()

usuario.remover_tarefa_de_lista('Pessoal', 'Livro')
