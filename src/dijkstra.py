def dijkstra(G, w, s):
    V, A = G
    dist = {}
    prev = {}

    for v in V:
        dist[v] = float('inf')
        prev[v] = None
    dist[s] = 0
    prev[s] = s

    O = set(V)
    C = set()

    while C != set(V):
        u = min(O, key=lambda x: dist[x])

        C.add(u)
        O.remove(u)

        for v in [vizinho for vizinho in V if (u, vizinho) in A and vizinho not in C]:
            if dist[v] > dist[u] + w[(u, v)]:
                dist[v] = dist[u] + w[(u, v)]
                prev[v] = u

    return dist, prev