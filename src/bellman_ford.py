def bellman_ford(G, w, s):
    V = list(G.keys())
    n = len(V)

    dist = {v: float('inf') for v in V}
    prev = {v: None for v in V}

    dist[s] = 0
    prev[s] = s

    for _ in range(n - 1):
        atualizou = False
        for u in V:
            for v in G[u]:
                if dist[v] > dist[u] + w[(u, v)]:
                    dist[v] = dist[u] + w[(u, v)]
                    prev[v] = u
                    atualizou = True
        if not atualizou:
            break

    return dist, prev
