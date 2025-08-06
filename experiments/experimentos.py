import random
import time
import tracemalloc
from statistics import mean

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


def rodar_bellman_10x(caminho_arquivo):
    G, w = carregar_grafo(caminho_arquivo)
    vertices = list(G.keys())

    custos = []
    tempos = []
    memorias = []