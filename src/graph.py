from typing import Dict, List, Tuple, Optional
import heapq
from collections import defaultdict

class Graph:
    """
    Classe para representar um grafo ponderado direcionado.
    """
    
    def __init__(self):
        """Inicializa um grafo vazio."""
        self.vertices = set()
        self.edges = defaultdict(list)  # {vertex: [(neighbor, weight), ...]}
        self.weights = {}  # {(u, v): weight}
    
    def add_vertex(self, vertex: int) -> None:
        """Adiciona um vértice ao grafo."""
        self.vertices.add(vertex)
    
    def add_edge(self, u: int, v: int, weight: float) -> None:
        """
        Adiciona uma aresta direcionada do vértice u para v com peso weight.
        
        Args:
            u: vértice de origem
            v: vértice de destino
            weight: peso da aresta
        """
        self.add_vertex(u)
        self.add_vertex(v)
        self.edges[u].append((v, weight))
        self.weights[(u, v)] = weight
    
    def get_neighbors(self, vertex: int) -> List[Tuple[int, float]]:
        """
        Retorna os vizinhos de um vértice com seus respectivos pesos.
        
        Args:
            vertex: vértice para obter os vizinhos
            
        Returns:
            Lista de tuplas (vizinho, peso)
        """
        return self.edges[vertex]
    
    def get_weight(self, u: int, v: int) -> Optional[float]:
        """
        Retorna o peso da aresta entre u e v.
        
        Args:
            u: vértice de origem
            v: vértice de destino
            
        Returns:
            Peso da aresta ou None se não existir
        """
        return self.weights.get((u, v))
    
    def get_vertices(self) -> set:
    # Retorna todos os vértices, inclusive os que só aparecem como destino
        vertices = set(self.vertices)
        for u in self.edges:
            vertices.add(u)
            for v, _ in self.edges[u]:
                vertices.add(v)
        return vertices
    
    def get_edges(self) -> List[Tuple[int, int, float]]:
        """
        Retorna todas as arestas do grafo.
        
        Returns:
            Lista de tuplas (origem, destino, peso)
        """
        edges = []
        for u in self.edges:
            for v, weight in self.edges[u]:
                edges.append((u, v, weight))
        return edges
    
    def __str__(self) -> str:
        """Representação em string do grafo."""
        result = f"Grafo com {len(self.vertices)} vértices e {len(self.get_edges())} arestas:\n"
        for u in sorted(self.edges.keys()):
            neighbors = self.edges[u]
            if neighbors:
                neighbor_str = ", ".join([f"{v}({w})" for v, w in neighbors])
                result += f"  {u} -> {neighbor_str}\n"
        return result
    
    @classmethod
    def from_file(cls, filename: str) -> 'Graph':
        """
        Cria um grafo a partir de um arquivo.
        
        Formato esperado:
        - Primeira linha: n_vertices n_edges
        - Linhas seguintes: u v weight (aresta do vértice u para v com peso weight)
        
        Args:
            filename: nome do arquivo
            
        Returns:
            Instância do grafo
        """
        graph = cls()
        
        with open(filename, 'r') as f:
            lines = f.readlines()
            
        if not lines:
            return graph
            
        # Primeira linha: número de vértices e arestas
        first_line = lines[0].strip().split()
        if len(first_line) >= 2:
            n_vertices, n_edges = map(int, first_line[:2])
            
            # Adicionar vértices
            for i in range(n_vertices):
                graph.add_vertex(i)
        
        # Adicionar arestas
        for line in lines[1:]:
            line = line.strip()
            if line:
                parts = line.split()
                if len(parts) >= 3:
                    u, v, weight = int(parts[0]), int(parts[1]), float(parts[2])
                    graph.add_edge(u, v, weight)
        
        return graph
