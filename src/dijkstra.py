import time
import psutil
import os
from typing import Dict, List, Tuple, Optional
from .graph import Graph

def dijkstra(graph: Graph, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Implementação do algoritmo de Dijkstra seguindo rigorosamente o pseudocódigo fornecido.
    
    Args:
        graph: Grafo ponderado direcionado
        source: Vértice de origem
        
    Returns:
        Tupla contendo:
        - dist: dicionário com as distâncias mínimas de source para cada vértice
        - prev: dicionário com os predecessores no caminho mínimo
    """
    V = graph.get_vertices()
    
    # Inicialização conforme pseudocódigo
    dist = {}
    prev = {}
    
    # Linha 1-5 do pseudocódigo
    for v in V:
        dist[v] = float('inf')
        prev[v] = None
    
    dist[source] = 0
    prev[source] = source
    
    # Linha 6-7 do pseudocódigo
    O = set(V)  # Conjunto de vértices abertos
    C = set()   # Conjunto de vértices fechados
    
    # Linha 8 do pseudocódigo: enquanto C != V
    while len(C) != len(V):
        # Linha 9 do pseudocódigo: encontrar vértice u em O com dist[u] mínimo
        u = min(O, key=lambda x: dist[x])
        
        # Linha 10-11 do pseudocódigo
        C.add(u)
        O.remove(u)
        
        # Linha 12 do pseudocódigo: para cada vizinho v de u tal que v não está em C
        for v, weight in graph.get_neighbors(u):
            if v not in C:  # v não está em C
                # Linha 13-15 do pseudocódigo
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    prev[v] = u
    
    return dist, prev

def get_shortest_path(prev: Dict[int, Optional[int]], source: int, target: int) -> List[int]:
    """
    Reconstrói o caminho mínimo de source para target usando o dicionário de predecessores.
    
    Args:
        prev: Dicionário de predecessores retornado por dijkstra
        source: Vértice de origem
        target: Vértice de destino
        
    Returns:
        Lista de vértices representando o caminho mínimo
    """
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

def dijkstra_with_metrics(graph: Graph, source: int, target: int) -> Dict:
    """
    Executa o algoritmo de Dijkstra e retorna métricas de tempo e memória.
    
    Args:
        graph: Grafo ponderado direcionado
        source: Vértice de origem
        target: Vértice de destino
        
    Returns:
        Dicionário com resultados e métricas
    """
    # Obter processo atual para monitoramento de memória
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    # Medir tempo de execução
    start_time = time.time()
    
    # Executar algoritmo de Dijkstra
    dist, prev = dijkstra(graph, source)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Calcular memória utilizada
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_used = final_memory - initial_memory
    
    # Reconstruir caminho
    path = get_shortest_path(prev, source, target)
    
    # Calcular custo do caminho
    cost = dist[target] if dist[target] != float('inf') else float('inf')
    
    return {
        'path': path,
        'cost': cost,
        'execution_time': execution_time,
        'memory_used': memory_used,
        'distances': dist,
        'predecessors': prev
    }
