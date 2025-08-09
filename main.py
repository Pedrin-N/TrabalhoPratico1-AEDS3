import sys
import time
import tracemalloc

from src.graph import carregar_grafo
from src.bellman_ford import bellman_ford
from src.dijkstra import dijkstra
from src.floyd_warshall import floyd_warshall

def reconstruir_caminho(prev, origem, destino):
    caminho = []
    atual = destino
    while atual != origem:
        if atual is None:
            return None
        caminho.append(atual)
        atual = prev[atual]
    caminho.append(origem)
    caminho.reverse()
    return caminho

def medir_execucao(algoritmo, G, w, origem, destino):
    tracemalloc.start()
    inicio = time.time()

    dist, prev = algoritmo(G, w, origem)
    caminho = reconstruir_caminho(prev, origem, destino)
    custo = dist[destino]

    fim = time.time()
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_exec = fim - inicio
    memoria_mb = mem_pico / (1024 * 1024)

    return caminho, custo, tempo_exec, memoria_mb

def reconstruir_caminho_fw(prev, origem, destino):
    if prev[(origem, destino)] is None:
        return None
    caminho = [destino]
    atual = destino
    while atual != origem:
        atual = prev[(origem, atual)]
        if atual is None:
            return None
        caminho.append(atual)
    caminho.reverse()
    return caminho

def medir_execucao_fw(algoritmo, G, w, origem, destino, V):
    tracemalloc.start()
    inicio = time.time()

    dist, prev = algoritmo(G, w)
    caminho = reconstruir_caminho_fw(prev, origem, destino)
    custo = dist[(origem, destino)]

    fim = time.time()
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_exec = fim - inicio
    memoria_mb = mem_pico / (1024 * 1024)

    return caminho, custo, tempo_exec, memoria_mb

def main():
    if len(sys.argv) != 4:
        print("Uso: python main.py <arquivo.txt> <origem> <destino>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    origem = int(sys.argv[2])
    destino = int(sys.argv[3])

    print(f"Carregando grafo de {nome_arquivo}...")
    G, w, V, A = carregar_grafo(nome_arquivo)
    print(f"Grafo carregado: {len(V)} vértices, {len(A)} arestas")

    caminho_bf, custo_bf, tempo_bf, memoria_bf = medir_execucao(bellman_ford, G, w, origem, destino)

    dijkstra_grafo = (V, A)
    caminho_dj, custo_dj, tempo_dj, memoria_dj = medir_execucao(dijkstra, dijkstra_grafo, w, origem, destino)
    
    caminho_fw, custo_fw, tempo_fw, memoria_fw = medir_execucao_fw(floyd_warshall, G, w, origem, destino, V)


    print("\nAlgoritmo de Bellman-Ford:")
    if caminho_bf is None:
        print("  Caminho mínimo: Não existe")
    else:
        print(f"  Caminho mínimo: {caminho_bf}")
        print(f"  Custo: {custo_bf}")
    print(f"  Tempo de execução: {tempo_bf:.6f} s")
    print(f"  Memória utilizada: {memoria_bf:.6f} MB")

    print("\nAlgoritmo de Dijkstra:")
    if caminho_dj is None:
        print("  Caminho mínimo: Não existe")
    else:
        print(f"  Caminho mínimo: {caminho_dj}")
        print(f"  Custo: {custo_dj}")
    print(f"  Tempo de execução: {tempo_dj:.6f} s")
    print(f"  Memória utilizada: {memoria_dj:.6f} MB")
    print("\nAlgoritmo de Floyd-Warshall:")
    if caminho_fw is None:
        print("  Caminho mínimo: Não existe")
    else:
        print(f"  Caminho mínimo: {caminho_fw}")
        print(f"  Custo: {custo_fw}")
    print(f"  Tempo de execução: {tempo_fw:.6f} s")
    print(f"  Memória utilizada: {memoria_fw:.6f} MB")

if __name__ == "__main__":
    main()
