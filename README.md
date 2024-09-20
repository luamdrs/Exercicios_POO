# 🩵 Exercícios sobre Classe e Métodos de Classe em Python 

### Você sabe qual é a diferença entre Método de Instância, Método de Classe e Método de Estância?



**Método de Instância**

_Definição: É o tipo de método mais comum em Python. Ele é associado a uma instância específica da classe e pode acessar e modificar os atributos da instância._

_Parâmetro: Sempre recebe self como primeiro parâmetro, que representa a própria instância._

_Uso: Quando a lógica do método depende dos atributos ou do estado de uma instância._

**Método de Classe**

_Definição: Está associado à própria classe, não a uma instância específica. Ele pode acessar e modificar atributos da classe, mas não os da instância diretamente._

_Parâmetro: Recebe cls como primeiro parâmetro, que faz referência à classe em si._

_Uso: Quando a lógica do método está relacionada à classe como um todo, como manter contadores ou acessar atributos compartilhados por todas as instâncias._

**Método Estático**

_Definição: É um método que não acessa nem a instância (self) nem a classe (cls). Ele é como uma função comum, mas que está logicamente relacionada à classe._

_Parâmetro: Não recebe nem self nem cls._

_Uso: Quando o método realiza uma operação que não depende de atributos da instância ou da classe, mas ainda faz sentido no contexto da classe._


#

📌 _Esses exercícios cobrem conceitos como contadores de instâncias, fábricas de objetos, controle de estoque e métodos de classe para gerenciamento de atributos globais._
