import sys
import time
import tracemalloc

from src.graph import carregar_grafo
from src.bellman_ford import bellman_ford


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


def medir_execucao_bellman(G, w, origem, destino):
    tracemalloc.start()
    inicio = time.time()

    dist, prev = bellman_ford(G, w, origem)
    caminho = reconstruir_caminho(prev, origem, destino)
    custo = dist[destino]

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

    G, w = carregar_grafo(nome_arquivo)

    caminho, custo, tempo_exec, memoria = medir_execucao_bellman(G, w, origem, destino)

    print(f"\nAlgoritmo de Bellman-Ford:")
    if caminho is None:
        print("  Caminho mínimo: Não existe")
    else:
        print(f"  Caminho mínimo: {caminho}")
        print(f"  Custo: {custo}")
    print(f"  Tempo de execução: {tempo_exec:.6f} s")
    print(f"  Memória utilizada: {memoria:.6f} MB")


if __name__ == "__main__":
    main()
