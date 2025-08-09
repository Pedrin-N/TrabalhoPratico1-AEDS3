#!/usr/bin/env python3
"""
Executa o algoritmo de Floyd-Warshall em um grafo da pasta data.
Uso: python main.py data/<arquivo> <origem> <destino>
"""

import sys
import os
from src.graph import Graph
from src.floyd_warshall import floyd_warshall_with_metrics

def print_usage():
    print("Uso: python main.py data/<arquivo> <origem> <destino>")
    print("Exemplo: python main.py data/toy.txt 0 3")

def main():
    if len(sys.argv) != 4:
        print("Erro: Número incorreto de argumentos.")
        print_usage()
        sys.exit(1)

    graph_file = sys.argv[1]
    try:
        source = int(sys.argv[2])
        target = int(sys.argv[3])
    except ValueError:
        print("Erro: Origem e destino devem ser inteiros.")
        sys.exit(1)

    if not os.path.exists(graph_file):
        print(f"Erro: Arquivo '{graph_file}' não encontrado.")
        sys.exit(1)

    print("Processando ...")
    print("-" * 80)

    try:
        graph = Graph.from_file(graph_file)
        vertices = graph.get_vertices()
        if source not in vertices:
            print(f"Erro: Vértice de origem {source} não existe no grafo.")
            print(f"Vértices disponíveis: {sorted(vertices)}")
            sys.exit(1)
        if target not in vertices:
            print(f"Erro: Vértice de destino {target} não existe no grafo.")
            print(f"Vértices disponíveis: {sorted(vertices)}")
            sys.exit(1)

        result = floyd_warshall_with_metrics(graph, source, target)

        print("-" * 65)
        print("Algoritmo de Floyd-Warshall:")
        print(f"Caminho mínimo: {result['path']}")
        if result['cost'] == float('inf'):
            print("Custo: ∞ (não há caminho)")
        else:
            print(f"Custo: {result['cost']}")
        print(f"Tempo execução: {result['execution_time']:.3f} s")
        print(f"Memória utilizada: {result['memory_used']:.4f} MB")
        print("-" * 65)

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        sys.exit(1)
    
    # ...existing code...

        graph = Graph.from_file(graph_file)
        vertices = graph.get_vertices()
        if len(vertices) > 1000:
            print("Aviso: Floyd-Warshall é inviável para grafos com mais de 1000 vértices.")
            sys.exit(1)
# ...restante do código...

    print("-" * 80)

if __name__ == "__main__":
    main()