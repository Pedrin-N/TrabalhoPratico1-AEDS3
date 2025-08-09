# Documentação da Implementação - Algoritmo de Floyd-Warshall

## Visão Geral

Este documento descreve a implementação do algoritmo de Floyd-Warshall, que resolve o problema dos caminhos mínimos entre todos os pares de vértices em um grafo ponderado. A implementação é baseada no pseudocódigo clássico do algoritmo.

## Estrutura do Código

### 1. Classe Graph (`src/graph.py`)
A classe `Graph` é a mesma, mas um método `get_weight(u, v)` é útil para a inicialização do Floyd-Warshall.

```python
class Graph:
    # ... (métodos existentes)
    def get_weight(self, u, v):
        # Retorna o peso da aresta (u, v) se existir
        if u in self.edges and v in [neighbor for neighbor, weight in self.edges[u]]:
            return self.weights[(u, v)]
        return None
```

### 2. Implementação do Floyd-Warshall (`src/floyd_warshall.py`)

#### Função Principal: `floyd_warshall(graph)`
A implementação utiliza programação dinâmica para resolver o problema.

```python
from typing import Dict, Tuple

def floyd_warshall(graph: Graph) -> Tuple[Dict, Dict]:
    V = list(graph.get_vertices())
    dist = {}
    prev = {}

    # 1. Fase de Inicialização
    for i in V:
        for j in V:
            if i == j:
                dist[(i, j)] = 0
                prev[(i, j)] = i
            elif graph.get_weight(i, j) is not None:
                dist[(i, j)] = graph.get_weight(i, j)
                prev[(i, j)] = i
            else:
                dist[(i, j)] = float('inf')
                prev[(i, j)] = None

    # 2. Algoritmo Principal (Loop triplo)
    for k in V:
        for i in V:
            for j in V:
                # Relaxamento da aresta (i, j) através de k
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
                    prev[(i, j)] = prev[(k, j)] # O predecessor de j no caminho via k

    return dist, prev
```

#### Correspondência com o Pseudocódigo

| Conceito do Pseudocódigo | Implementação Python |
| :--- | :--- |
| Inicialização das matrizes `dist` e `prev` | Primeiro laço duplo (`for i in V: for j in V:`) |
| Laço principal sobre os vértices intermediários | `for k in V:` |
| Laços sobre os vértices de origem e destino | `for i in V:` e `for j in V:` |
| Relaxamento (atualização da distância) | `if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]` |


### 3. Funções Auxiliares

#### `get_fw_path(prev, source, target)`
Reconstrói o caminho a partir da matriz de predecessores. A lógica de reconstrução para Floyd-Warshall é diferente da de Dijkstra.

```python
from typing import Dict, List

def get_fw_path(prev: Dict, source: int, target: int) -> List[int]:
    if prev.get((source, target)) is None:
        return []  # Não há caminho
    path = [target]
    while source != target:
        target = prev[(source, target)]
        if target is None: return [] # Caminho quebrado
        path.append(target)
    return list(reversed(path))
```

#### `floyd_warshall_with_metrics(graph, source, target)`
Executa o algoritmo, coleta métricas e retorna o caminho para um par específico (`source`, `target`).

```python
import psutil
import os
import time

def floyd_warshall_with_metrics(graph: Graph, source: int, target: int) -> Dict:
    # Monitoramento de memória e tempo
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss
    start_time = time.time()
    
    dist, prev = floyd_warshall(graph)
    
    execution_time = time.time() - start_time
    memory_used = process.memory_info().rss - initial_memory
    
    # Reconstrução do caminho para o par (source, target)
    path = get_fw_path(prev, source, target)
    cost = dist.get((source, target), float('inf'))
    
    return {
        'path': path, 'cost': cost,
        'execution_time': execution_time,
        'memory_used': memory_used / (1024 * 1024) # MB
    }
```

## Estruturas de Dados Utilizadas

- **Dicionários como Matrizes**: `Dict[Tuple[int, int], float]` é usado para representar as matrizes de distância e predecessores. Isso oferece flexibilidade, embora uma matriz NumPy pudesse ser mais performática em CPython para grafos densos.
- **Listas (Lists)**: Usadas para armazenar o caminho reconstruído.

## Complexidade Computacional

### Análise da Implementação

**Tempo: $O(V^3)$**

A complexidade é dominada pelos três laços aninhados (`for k in V`, `for i in V`, `for j in V`), cada um executando $V$ vezes. Isso resulta em uma complexidade cúbica, independente da densidade do grafo.

**Espaço: $O(V^2)$**

A implementação requer duas matrizes (representadas por dicionários) de tamanho $V \times V$ para armazenar as distâncias (`dist`) e os predecessores (`prev`).

## Conclusões da Implementação

1.  **Corretude**: A implementação segue fielmente o algoritmo clássico de Floyd-Warshall.
2.  **Simplicidade**: O código é relativamente simples e direto de entender.
3.  **Performance**: A performance é limitada pela alta complexidade computacional, tornando-a inadequada para grafos com mais de algumas centenas de vértices.
4.  **Escalabilidade**: O algoritmo não escala bem com o aumento do número de vértices.

## Limitações e Melhorias Futuras

### Limitações Atuais
1. Complexidade $O(V^3)$ torna o algoritmo lento para grafos grandes.
2. Complexidade de espaço $O(V^2)$ pode ser um problema em ambientes com memória limitada.
3. A implementação não detecta ciclos de peso negativo, embora o algoritmo possa ser adaptado para isso.

### Melhorias Possíveis
1. **Paralelização**: Os laços internos do algoritmo podem ser paralelizados para acelerar a execução em hardware com múltiplos núcleos.
2. **Uso de NumPy**: Para grafos cujos vértices são inteiros sequenciais, o uso de arrays NumPy em vez de dicionários pode oferecer uma melhoria de performance significativa.