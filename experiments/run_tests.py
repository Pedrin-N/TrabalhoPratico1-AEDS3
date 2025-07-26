#!/usr/bin/env python3
"""
Script para execução dos experimentos computacionais.
Calcula médias de tempo, memória e custo para o algoritmo de Dijkstra em diferentes grafos.
"""

import sys
import os
import random
import time
import csv
from typing import List, Dict, Tuple

# Adicionar o diretório pai ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.graph import Graph
from src.dijkstra import dijkstra_with_metrics

# Configuração dos experimentos
NUM_EXECUTIONS = 10  # Número de execuções por grafo
TIMEOUT_SECONDS = 600  # Timeout de 10 minutos
MEMORY_LIMIT_MB = 8000  # Limite de memória de 8GB

# Lista de grafos para teste
GRAPHS = [
    ("toy.txt", "Grafo pequeno para verificação manual"),
    ("facebook_combined.txt", "Conexões entre perfis do Facebook"),
    ("rg300_768.txt", "Grafo aleatório com 300 vértices e 768 arestas"),
    ("rg300_4730.txt", "Grafo aleatório com 300 vértices e 4730 arestas"),
    ("rome99c.txt", "Mapa das estradas de Roma em 1999"),
    ("USA-road-dt.DC.txt", "Mapa das estradas de Washington DC")
]

def get_random_vertices(graph: Graph, num_pairs: int) -> List[Tuple[int, int]]:
    """
    Gera pares aleatórios de vértices origem-destino.
    
    Args:
        graph: Grafo para gerar os pares
        num_pairs: Número de pares a gerar
        
    Returns:
        Lista de tuplas (origem, destino)
    """
    vertices = list(graph.get_vertices())
    pairs = []
    
    for _ in range(num_pairs):
        source = random.choice(vertices)
        target = random.choice(vertices)
        while target == source:  # Evitar origem = destino
            target = random.choice(vertices)
        pairs.append((source, target))
    
    return pairs

def run_single_test(graph: Graph, source: int, target: int) -> Dict:
    """
    Executa um único teste do algoritmo de Dijkstra.
    
    Args:
        graph: Grafo para teste
        source: Vértice de origem
        target: Vértice de destino
        
    Returns:
        Dicionário com resultados do teste
    """
    try:
        result = dijkstra_with_metrics(graph, source, target)
        return {
            'success': True,
            'execution_time': result['execution_time'],
            'memory_used': result['memory_used'],
            'cost': result['cost'],
            'path_length': len(result['path']) if result['path'] else 0
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'execution_time': 0,
            'memory_used': 0,
            'cost': float('inf'),
            'path_length': 0
        }

def run_experiments_for_graph(graph_file: str, graph_name: str) -> Dict:
    """
    Executa experimentos para um grafo específico.
    
    Args:
        graph_file: Caminho para o arquivo do grafo
        graph_name: Nome descritivo do grafo
        
    Returns:
        Dicionário com resultados dos experimentos
    """
    print(f"\nExecutando experimentos para: {graph_name}")
    print(f"Arquivo: {graph_file}")
    
    # Verificar se o arquivo existe
    if not os.path.exists(graph_file):
        print(f"  ERRO: Arquivo {graph_file} não encontrado!")
        return {
            'graph_name': graph_name,
            'file_exists': False,
            'avg_time': 'ARQUIVO NÃO ENCONTRADO',
            'avg_memory': 'ARQUIVO NÃO ENCONTRADO',
            'avg_cost': 'ARQUIVO NÃO ENCONTRADO'
        }
    
    try:
        # Carregar grafo
        print("  Carregando grafo...")
        graph = Graph.from_file(graph_file)
        vertices = graph.get_vertices()
        print(f"  Grafo carregado: {len(vertices)} vértices, {len(graph.get_edges())} arestas")
        
        # Gerar pares de vértices para teste
        vertex_pairs = get_random_vertices(graph, NUM_EXECUTIONS)
        
        # Executar testes
        results = []
        for i, (source, target) in enumerate(vertex_pairs, 1):
            print(f"  Teste {i}/{NUM_EXECUTIONS}: {source} -> {target}")
            
            result = run_single_test(graph, source, target)
            results.append(result)
            
            if not result['success']:
                print(f"    ERRO: {result['error']}")
            else:
                print(f"    Tempo: {result['execution_time']:.6f}s, "
                      f"Memória: {result['memory_used']:.6f}MB, "
                      f"Custo: {result['cost']}")
        
        # Calcular estatísticas
        successful_results = [r for r in results if r['success']]
        
        if not successful_results:
            return {
                'graph_name': graph_name,
                'file_exists': True,
                'avg_time': 'TODOS FALHARAM',
                'avg_memory': 'TODOS FALHARAM',
                'avg_cost': 'TODOS FALHARAM'
            }
        
        avg_time = sum(r['execution_time'] for r in successful_results) / len(successful_results)
        avg_memory = sum(r['memory_used'] for r in successful_results) / len(successful_results)
        avg_cost = sum(r['cost'] for r in successful_results if r['cost'] != float('inf')) / len([r for r in successful_results if r['cost'] != float('inf')])
        
        # Verificar timeouts e limites de memória
        if avg_time > TIMEOUT_SECONDS:
            avg_time_str = 'TEMPO LIMITE'
        else:
            avg_time_str = f"{avg_time:.6f}"
        
        if avg_memory > MEMORY_LIMIT_MB:
            avg_memory_str = 'MEMORIA EXCEDIDA'
        else:
            avg_memory_str = f"{avg_memory:.6f}"
        
        return {
            'graph_name': graph_name,
            'file_exists': True,
            'avg_time': avg_time_str,
            'avg_memory': avg_memory_str,
            'avg_cost': f"{avg_cost:.2f}" if avg_cost != float('inf') else "∞",
            'success_rate': f"{len(successful_results)}/{NUM_EXECUTIONS}"
        }
        
    except Exception as e:
        print(f"  ERRO ao processar grafo: {e}")
        return {
            'graph_name': graph_name,
            'file_exists': True,
            'avg_time': 'ERRO',
            'avg_memory': 'ERRO',
            'avg_cost': 'ERRO',
            'error': str(e)
        }

def save_results_to_csv(results: List[Dict], filename: str = "results.csv"):
    """
    Salva os resultados em arquivo CSV.
    
    Args:
        results: Lista de resultados dos experimentos
        filename: Nome do arquivo CSV
    """
    csv_file = os.path.join(os.path.dirname(__file__), filename)
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Cabeçalho
        writer.writerow(['Grafo', 'T.médio (s)', 'M.média (MB)', 'Custo médio', 'Taxa de Sucesso'])
        
        # Dados
        for result in results:
            writer.writerow([
                result['graph_name'],
                result['avg_time'],
                result['avg_memory'],
                result['avg_cost'],
                result.get('success_rate', 'N/A')
            ])
    
    print(f"\nResultados salvos em: {csv_file}")

def main():
    """Função principal dos experimentos."""
    print("=" * 80)
    print("EXPERIMENTOS COMPUTACIONAIS - ALGORITMO DE DIJKSTRA")
    print("=" * 80)
    print(f"Número de execuções por grafo: {NUM_EXECUTIONS}")
    print(f"Timeout: {TIMEOUT_SECONDS} segundos")
    print(f"Limite de memória: {MEMORY_LIMIT_MB} MB")
    print("=" * 80)
    
    # Configurar seed para reprodutibilidade
    random.seed(42)
    
    # Executar experimentos para cada grafo
    all_results = []
    
    for graph_file, graph_name in GRAPHS:
        # Construir caminho completo para o arquivo
        full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', graph_file)
        
        result = run_experiments_for_graph(full_path, graph_name)
        all_results.append(result)
    
    # Salvar resultados
    save_results_to_csv(all_results)
    
    # Exibir resumo
    print("\n" + "=" * 80)
    print("RESUMO DOS RESULTADOS")
    print("=" * 80)
    print(f"{'Grafo':<25} {'T.médio (s)':<15} {'M.média (MB)':<15} {'Custo médio':<15}")
    print("-" * 80)
    
    for result in all_results:
        print(f"{result['graph_name']:<25} {result['avg_time']:<15} {result['avg_memory']:<15} {result['avg_cost']:<15}")
    
    print("=" * 80)
    print("Experimentos concluídos!")

if __name__ == "__main__":
    main()
