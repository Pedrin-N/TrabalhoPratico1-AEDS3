import time
import psutil
import os
from typing import Dict, List, Tuple, Optional
from .graph import Graph

def floyd_warshall(graph: Graph) -> Tuple[Dict[Tuple[int, int], float], Dict[Tuple[int, int], Optional[int]]]:
    V = list(graph.get_vertices())
    dist: Dict[Tuple[int, int], float] = {}
    prev: Dict[Tuple[int, int], Optional[int]] = {}

    # Inicialização
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

    # Algoritmo principal
    for k in V:
        for i in V:
            for j in V:
                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
                    prev[(i, j)] = prev[(k, j)]

    return dist, prev  # <-- ESSA LINHA É OBRIGATÓRIA
    

def get_fw_path(prev: Dict[Tuple[int, int], Optional[int]], source: int, target: int) -> List[int]:
    """
    Reconstrói o caminho mínimo de source para target usando o dicionário de predecessores do Floyd-Warshall.
    """
    if prev[(source, target)] is None:
        return []
    path = [target]
    while target != source:
        target = prev[(source, target)]
        if target is None:
            return []
        path.append(target)
    path.reverse()
    return path

def floyd_warshall_with_metrics(graph: Graph, source: int, target: int) -> Dict:
    """
    Executa Floyd-Warshall e retorna métricas de tempo e memória.
    """
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB

    start_time = time.time()
    dist, prev = floyd_warshall(graph)
    end_time = time.time()
    execution_time = end_time - start_time

    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_used = final_memory - initial_memory

    path = get_fw_path(prev, source, target)
    cost = dist[(source, target)] if dist[(source, target)] != float('inf') else float('inf')

    return {
        'path': path,
        'cost': cost,
        'execution_time': execution_time,
        'memory_used': memory_used,
        'distances': dist,
        'predecessors': prev
    }