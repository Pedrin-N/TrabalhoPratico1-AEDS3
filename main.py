#!/usr/bin/env python3
"""
Programa principal para execução do algoritmo de Dijkstra.
Recebe parâmetros via linha de comando: arquivo_grafo, vértice_origem, vértice_destino.
"""

import sys
import os
from unittest import result
from src.graph import Graph
from src.dijkstra import dijkstra_with_metrics

def print_usage():
    """Exibe instruções de uso do programa."""
    print("Uso: python main.py <arquivo_grafo> <vértice_origem> <vértice_destino>")
    print("Exemplo: python main.py data/toy.txt 0 3")
    print("\nDescrição:")
    print("  arquivo_grafo: arquivo contendo o grafo no formato DIMACS")
    print("  vértice_origem: vértice de origem (número inteiro)")
    print("  vértice_destino: vértice de destino (número inteiro)")

def validate_arguments():
    """Valida os argumentos da linha de comando."""
    if len(sys.argv) != 4:
        print("Erro: Número incorreto de argumentos.")
        print_usage()
        return False, None, None, None
    
    graph_file = sys.argv[1]
    try:
        source = int(sys.argv[2])
        target = int(sys.argv[3])
    except ValueError:
        print("Erro: Vértices de origem e destino devem ser números inteiros.")
        return False, None, None, None
    
    if not os.path.exists(graph_file):
        print(f"Erro: Arquivo '{graph_file}' não encontrado.")
        return False, None, None, None
    
    return True, graph_file, source, target

def main():
    """Função principal do programa."""
    # Validar argumentos
    valid, graph_file, source, target = validate_arguments()
    if not valid:
        sys.exit(1)
    
    print("Processando ...")
    print("-" * 80)
    
    try:
        # Carregar grafo do arquivo
        graph = Graph.from_file(graph_file)
        
        # Verificar se os vértices existem no grafo
        vertices = graph.get_vertices()
        if source not in vertices:
            print(f"Erro: Vértice de origem {source} não existe no grafo.")
            print(f"Vértices disponíveis: {sorted(vertices)}")
            sys.exit(1)
        
        if target not in vertices:
            print(f"Erro: Vértice de destino {target} não existe no grafo.")
            print(f"Vértices disponíveis: {sorted(vertices)}")
            sys.exit(1)
        
        # Executar algoritmo de Dijkstra
        result = dijkstra_with_metrics(graph, source, target)
        
        # Exibir resultados
        print("-" * 65)
        print("Algoritmo de Dijkstra:")
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
    
    print("-" * 80)

if __name__ == "__main__":
    main()
