from abc import ABC, abstractmethod

# Princípio de Responsabilidade Única (SRP): A classe Tarefa lida apenas com dados e status da tarefa.
class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

# Princípio Aberto/Fechado (OCP): RepositorioTarefas é uma interface que permite estender o sistema com novos repositórios, como RepositorioBancoDeDados e RepositorioArquivoJson, sem alterar o código do GestorDeTarefas.
class RepositorioTarefas(ABC):
    @abstractmethod
    def salvar(self, tarefa: Tarefa):
        pass

    @abstractmethod
    def listar(self):
        pass

# Princípio de Substituição de Liskov (LSP): RepositorioBancoDeDados e RepositorioArquivoJson são substituíveis por RepositorioTarefas onde necessário.
class RepositorioBancoDeDados(RepositorioTarefas):
    def __init__(self):
        self.banco = []

    def salvar(self, tarefa: Tarefa):
        self.banco.append(tarefa)
        print(f'Tarefa "{tarefa.titulo}" salva no banco de dados.')
    
    def listar(self):
        return self.banco

class RepositorioArquivoJson(RepositorioTarefas):
    def __init__(self):
        self.arquivo = []

    def salvar(self, tarefa: Tarefa):
        self.arquivo.append(tarefa)
        print(f'Tarefa "{tarefa.titulo}" salva em um arquivo JSON.')

    def listar(self):
        return self.arquivo

# Princípio de Segregação de Interface (ISP): TarefaConcluivel define uma interface específica para concluir tarefas, evitando que classes dependam de métodos que não utilizam.
class TarefaConcluivel(ABC):
    @abstractmethod
    def concluir_tarefa(self, tarefa: Tarefa):
        pass

# GestorDeTarefas depende da abstração RepositorioTarefas, e não de implementações concretas, permitindo a injeção de dependência.
class GestorDeTarefas(TarefaConcluivel):
    def __init__(self, repositorio: RepositorioTarefas):
        self.repositorio = repositorio

    def adicionar_tarefa(self, tarefa: Tarefa):
        self.repositorio.salvar(tarefa)

    def listar_tarefas(self):
        return self.repositorio.listar()

    def concluir_tarefa(self, tarefa: Tarefa):
        tarefa.marcar_concluida()
        print(f'Tarefa "{tarefa.titulo}" marcada como concluída.')

tarefa1 = Tarefa('Estudar SOLID', 'Revisar cada princípio SOLID em um exemplo de código.')
tarefa2 = Tarefa('Implementar sistema de tarefas', 'Aplicar SOLID em um projeto de tarefas.')

repositorio_bd = RepositorioBancoDeDados()
gestor_tarefas_bd = GestorDeTarefas(repositorio_bd)

gestor_tarefas_bd.adicionar_tarefa(tarefa1)
gestor_tarefas_bd.adicionar_tarefa(tarefa2)
gestor_tarefas_bd.concluir_tarefa(tarefa1)

print('\nLista de Tarefas:')
for tarefa in gestor_tarefas_bd.listar_tarefas():
    status = 'Concluída' if tarefa.concluida else 'Pendente'
    print(f'{tarefa.titulo} - {status}')