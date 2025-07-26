# Documentação da Implementação - Algoritmo de Dijkstra

## Visão Geral

Este documento descreve a implementação do algoritmo de Dijkstra realizada conforme as especificações do trabalho prático da disciplina CSI115 - Algoritmos e Estruturas de Dados III. A implementação segue rigorosamente o pseudocódigo fornecido e utiliza estruturas de dados apropriadas para garantir eficiência e corretude.

## Estrutura do Código

### 1. Classe Graph (`src/graph.py`)

A classe `Graph` fornece a representação fundamental do grafo ponderado direcionado:

```python
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.weights = {}
```

**Métodos principais:**
- `add_vertex(vertex)`: Adiciona um vértice ao grafo
- `add_edge(u, v, weight)`: Adiciona uma aresta direcionada com peso
- `get_vertices()`: Retorna o conjunto de vértices
- `get_neighbors(vertex)`: Retorna os vizinhos de um vértice
- `from_file(filename)`: Carrega grafo de arquivo no formato DIMACS

### 2. Implementação do Dijkstra (`src/dijkstra.py`)

#### Função Principal: `dijkstra(graph, source)`

A implementação segue exatamente o pseudocódigo fornecido:

```python
def dijkstra(graph: Graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    V = graph.get_vertices()
    
    # Inicialização (linhas 1-5 do pseudocódigo)
    dist = {}
    prev = {}
    for v in V:
        dist[v] = float('inf')
        prev[v] = None
    dist[source] = 0
    prev[source] = source
    
    # Conjuntos O e C (linhas 6-7 do pseudocódigo)
    O = set(V)  # Vértices abertos
    C = set()   # Vértices fechados
    
    # Loop principal (linha 8 do pseudocódigo)
    while len(C) != len(V):
        # Encontrar vértice u em O com dist[u] mínimo (linha 9)
        u = min(O, key=lambda x: dist[x])
        
        # Mover u de O para C (linhas 10-11)
        C.add(u)
        O.remove(u)
        
        # Para cada vizinho v de u tal que v não está em C (linha 12)
        for v, weight in graph.get_neighbors(u):
            if v not in C:  # v não está em C
                # Relaxamento (linhas 13-15)
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    prev[v] = u
    
    return dist, prev
```

#### Correspondência com o Pseudocódigo

| Linha do Pseudocódigo | Implementação Python |
|----------------------|---------------------|
| 1-5 | Inicialização de `dist` e `prev` |
| 6-7 | Criação dos conjuntos `O` e `C` |
| 8 | Loop `while len(C) != len(V)` |
| 9 | `u = min(O, key=lambda x: dist[x])` |
| 10-11 | `C.add(u)` e `O.remove(u)` |
| 12 | Loop sobre vizinhos com verificação `v not in C` |
| 13-15 | Condição e atualização de `dist[v]` e `prev[v]` |

### 3. Funções Auxiliares

#### `get_shortest_path(prev, source, target)`

Reconstrói o caminho mínimo usando o dicionário de predecessores:

```python
def get_shortest_path(prev: Dict[int, Optional[int]], source: int, target: int) -> List[int]:
    if prev[target] is None:
        return []  # Não há caminho
    
    path = []
    current = target
    
    while current != source:
        path.append(current)
        current = prev[current]
        if current is None:
            return []  # Não há caminho
    
    path.append(source)
    return list(reversed(path))
```

#### `dijkstra_with_metrics(graph, source, target)`

Executa o algoritmo e coleta métricas de performance:

```python
def dijkstra_with_metrics(graph: Graph, source: int, target: int) -> Dict:
    # Monitoramento de memória
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024
    
    # Medição de tempo
    start_time = time.time()
    dist, prev = dijkstra(graph, source)
    end_time = time.time()
    
    # Cálculo de métricas
    execution_time = end_time - start_time
    final_memory = process.memory_info().rss / 1024 / 1024
    memory_used = final_memory - initial_memory
    
    # Reconstrução do caminho
    path = get_shortest_path(prev, source, target)
    cost = dist[target] if dist[target] != float('inf') else float('inf')
    
    return {
        'path': path,
        'cost': cost,
        'execution_time': execution_time,
        'memory_used': memory_used,
        'distances': dist,
        'predecessors': prev
    }
```

## Programa Principal (`main.py`)

### Estrutura do Programa

```python
def main():
    # Validação de argumentos
    valid, graph_file, source, target = validate_arguments()
    
    # Carregamento do grafo
    graph = Graph.from_file(graph_file)
    
    # Verificação de vértices
    vertices = graph.get_vertices()
    if source not in vertices or target not in vertices:
        # Tratamento de erro
    
    # Execução do algoritmo
    result = dijkstra_with_metrics(graph, source, target)
    
    # Exibição dos resultados
    print("Algoritmo de Dijkstra:")
    print(f"Caminho mínimo: {result['path']}")
    print(f"Custo: {result['cost']}")
    print(f"Tempo execução: {result['execution_time']:.6f} s")
    print(f"Memória utilizada: {result['memory_used']:.6f} MB")
```

### Validação de Entrada

O programa valida:
- Número correto de argumentos (3: arquivo, origem, destino)
- Existência do arquivo de grafo
- Vértices de origem e destino como números inteiros
- Existência dos vértices no grafo

## Script de Experimentos (`experiments/run_tests.py`)

### Configuração dos Experimentos

```python
NUM_EXECUTIONS = 10  # Execuções por grafo
TIMEOUT_SECONDS = 600  # Timeout de 10 minutos
MEMORY_LIMIT_MB = 8000  # Limite de memória de 8GB
```

### Processo de Execução

1. **Carregamento do grafo**: `Graph.from_file(graph_file)`
2. **Geração de pares aleatórios**: `get_random_vertices(graph, NUM_EXECUTIONS)`
3. **Execução dos testes**: `dijkstra_with_metrics(graph, source, target)`
4. **Coleta de estatísticas**: Médias de tempo, memória e custo
5. **Verificação de limites**: Timeout e limite de memória
6. **Geração de relatório**: Arquivo CSV com resultados

## Estruturas de Dados Utilizadas

### 1. Conjuntos (Sets)
- **Vértices**: `set()` para armazenar vértices únicos
- **Conjunto O (aberto)**: `set(V)` para vértices não processados
- **Conjunto C (fechado)**: `set()` para vértices processados

### 2. Dicionários (Dictionaries)
- **Distâncias**: `Dict[int, float]` para armazenar distâncias mínimas
- **Predecessores**: `Dict[int, Optional[int]]` para reconstruir caminhos
- **Arestas**: `defaultdict(list)` para representar adjacências

### 3. Listas (Lists)
- **Caminhos**: `List[int]` para representar sequências de vértices
- **Vizinhos**: `List[Tuple[int, float]]` para pares (vértice, peso)

## Tratamento de Casos Especiais

### 1. Vértices Inalcançáveis
- Distância inicializada como `float('inf')`
- Predecessor inicializado como `None`
- Caminho retornado como lista vazia `[]`

### 2. Vértice de Origem Igual ao Destino
- Distância zero
- Caminho contém apenas o vértice de origem
- Custo zero

### 3. Grafos Vazios ou Inválidos
- Validação de entrada no programa principal
- Tratamento de exceções durante carregamento
- Mensagens de erro informativas

## Otimizações Implementadas

### 1. Estrutura de Dados Eficiente
- Uso de `defaultdict` para evitar verificações de chave
- Conjuntos para operações O(1) de pertinência
- Dicionários para acesso O(1) a distâncias e predecessores

### 2. Monitoramento de Recursos
- Medição precisa de tempo usando `time.time()`
- Monitoramento de memória usando `psutil`
- Detecção de timeouts e limites de memória

### 3. Validação Robusta
- Verificação de existência de arquivos
- Validação de vértices de entrada
- Tratamento de erros com mensagens claras

## Complexidade Computacional

### Análise da Implementação

**Tempo:**
- Inicialização: O(V)
- Loop principal: O(V²) no pior caso
- Total: O(V²)

**Espaço:**
- Distâncias: O(V)
- Predecessores: O(V)
- Conjuntos O e C: O(V)
- Total: O(V)

### Comparação com Implementações Otimizadas

A implementação atual usa lista simples para encontrar o mínimo, resultando em complexidade O(V²). Implementações com heap binário poderiam reduzir para O((V + E) log V).

## Testes e Validação

### 1. Testes Unitários
- Verificação de grafos pequenos com resultados conhecidos
- Teste de casos extremos (vértices isolados, ciclos)
- Validação de caminhos mínimos

### 2. Testes de Performance
- Execução em grafos de diferentes tamanhos
- Medição de tempo e memória
- Verificação de escalabilidade

### 3. Testes de Robustez
- Tratamento de arquivos inexistentes
- Validação de entrada inválida
- Verificação de limites de recursos

## Conclusões da Implementação

1. **Corretude**: A implementação segue rigorosamente o pseudocódigo fornecido
2. **Eficiência**: Performance adequada para grafos de tamanho realista
3. **Robustez**: Tratamento adequado de casos especiais e erros
4. **Escalabilidade**: Funciona bem até grafos com ~10.000 vértices
5. **Manutenibilidade**: Código bem estruturado e documentado

## Limitações e Melhorias Futuras

### Limitações Atuais
1. Complexidade O(V²) devido ao uso de lista simples
2. Não otimizado para grafos muito densos
3. Implementação sequencial (não paralela)

### Melhorias Possíveis
1. Implementação com heap binário para O((V + E) log V)
2. Otimizações para grafos específicos (esparsos/densos)
3. Implementação paralela para grafos muito grandes
4. Cache de resultados para consultas repetidas 