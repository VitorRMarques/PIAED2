# Estruturas de Dados Utilizadas no Sistema de Gerenciamento de Ocorrências

## 1. Lista

As listas foram utilizadas como estrutura principal para armazenamento das ocorrências cadastradas no sistema.

### Aplicação

Foram utilizadas três listas:

```python
ocorrencia_lista
ocorrencia_lista_abertas
ocorrencia_lista_fechadas
```

### Função

* Armazenar todas as ocorrências cadastradas.
* Separar ocorrências abertas das ocorrências já atendidas.
* Permitir listagens completas das ocorrências.

### Vantagens

* Fácil inserção de novos elementos.
* Estrutura simples de implementar.
* Adequada para percorrer e exibir registros.

---

## 2. Fila (Queue)

A fila foi utilizada para realizar o atendimento das ocorrências por ordem de chegada.

### Implementação

```python
from collections import deque

fila_ocorrencias = deque()
```

### Funcionamento

A fila segue a política:

**FIFO (First In, First Out)**

Ou seja:

* A primeira ocorrência cadastrada é a primeira a ser atendida.
* Novas ocorrências entram no final da fila.
* O atendimento remove a ocorrência do início da fila.

### Operações utilizadas

Inserção:

```python
fila_ocorrencias.append(ocorrencia)
```

Remoção:

```python
fila_ocorrencias.popleft()
```

### Vantagens

* Mantém a ordem de chegada.
* Simula corretamente processos de atendimento reais.

---

## 3. Pilha (Stack)

A pilha foi utilizada para armazenar o histórico de ações realizadas no sistema.

### Implementação

```python
historico_acoes = []
```

### Funcionamento

A pilha segue a política:

**LIFO (Last In, First Out)**

Ou seja:

* A última ação realizada é a primeira a ser desfeita.

### Operações utilizadas

Empilhar ação:

```python
historico_acoes.append(acao)
```

Desempilhar ação:

```python
historico_acoes.pop()
```

### Aplicação

Foi utilizada para:

* Registrar cadastros.
* Registrar atendimentos.
* Registrar ordenações.
* Permitir a funcionalidade de desfazer ações.

### Vantagens

* Implementação simples.
* Ideal para sistemas de Undo/Redo.

---

## 4. Árvore Binária de Busca (BST)

A Árvore Binária de Busca foi utilizada para realizar buscas rápidas por ID da ocorrência.

### Estrutura

Cada nó da árvore armazena:

```python
class No:
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia
        self.esquerda = None
        self.direita = None
```

### Funcionamento

Ao cadastrar uma ocorrência:

```python
arvore_ids.inserir(ocorrencia)
```

A ocorrência é posicionada na árvore de acordo com seu identificador.

Na busca:

```python
arvore_ids.buscar(id)
```

o algoritmo percorre apenas os caminhos necessários até encontrar o elemento.

### Complexidade

| Operação | Complexidade Média |
| -------- | ------------------ |
| Inserção | O(log n)           |
| Busca    | O(log n)           |

### Vantagens

* Busca mais eficiente que uma lista.
* Organiza os elementos hierarquicamente.
* Reduz o número de comparações necessárias.

---

## 5. Hash Table

A Hash Table foi utilizada para indexar ocorrências por nome do solicitante e por tipo da ocorrência.

### Implementação

```python
indice_nome = {}
indice_tipo = {}
```

### Funcionamento

Quando uma ocorrência é cadastrada:

```python
indice_nome[nome].append(ocorrencia)
indice_tipo[tipo].append(ocorrencia)
```

Os dicionários armazenam referências para as ocorrências associadas a cada chave.

Exemplo:

```python
{
    "joao": [ocorrencia1, ocorrencia2],
    "maria": [ocorrencia3]
}
```

### Busca

Por nome:

```python
indice_nome.get(nome)
```

Por tipo:

```python
indice_tipo.get(tipo)
```

### Complexidade

| Operação | Complexidade Média |
| -------- | ------------------ |
| Inserção | O(1)               |
| Busca    | O(1)               |

### Vantagens

* Acesso extremamente rápido.
* Evita percorrer toda a lista de ocorrências.
* Escala melhor conforme o número de registros aumenta.

---

## 6. Heap (Fila de Prioridade)

A Heap foi utilizada para atender primeiro as ocorrências de maior prioridade.

### Implementação

```python
import heapq

heap_prioridades = []
```

### Funcionamento

Cada ocorrência é inserida na heap utilizando:

```python
heapq.heappush(
    heap_prioridades,
    (
        -int(prioridade),
        ordem_chegada,
        ocorrencia
    )
)
```

O valor da prioridade é armazenado de forma negativa para transformar a min-heap do Python em uma max-heap.

### Atendimento

```python
heapq.heappop(heap_prioridades)
```

Sempre retorna a ocorrência de maior prioridade.

Em caso de empate, a ordem de chegada é utilizada como critério de desempate.

### Complexidade

| Operação                     | Complexidade |
| ---------------------------- | ------------ |
| Inserção                     | O(log n)     |
| Remoção                      | O(log n)     |
| Consulta da maior prioridade | O(1)         |

### Vantagens

* Atendimento rápido das ocorrências críticas.
* Mantém automaticamente a ordem de prioridade.
* Mais eficiente do que procurar a maior prioridade em uma lista.

---

# Conclusão

O sistema utiliza diferentes estruturas de dados para resolver problemas específicos:

| Estrutura                     | Finalidade                       |
| ----------------------------- | -------------------------------- |
| Lista                         | Armazenamento das ocorrências    |
| Fila (Queue)                  | Atendimento por ordem de chegada |
| Pilha (Stack)                 | Histórico e desfazer ações       |
| Árvore Binária de Busca (BST) | Busca por ID                     |
| Hash Table                    | Busca por nome e tipo            |
| Heap                          | Atendimento por prioridade       |

A utilização dessas estruturas permitiu desenvolver um sistema mais organizado, eficiente e adequado para diferentes tipos de operações realizadas sobre as ocorrências.
