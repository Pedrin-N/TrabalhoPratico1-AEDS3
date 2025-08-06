def carregar_grafo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    n, m = map(int, linhas[0].split())
    G = {i: [] for i in range(n)}
    w = {}

    for linha in linhas[1:]:
        u, v, peso = map(int, linha.split())
        G[u].append(v)
        w[(u, v)] = peso

    return G, w
