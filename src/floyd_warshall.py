def floyd_warshall(G, w, origem=None, destino=None):
    V = list(G.keys())

    dist = {}
    prev = {}

    for i in V:
        for j in V:
            if i == j:
                dist[(i,j)] = 0
                prev[(i,j)] = i
            elif (i,j) in w:
                dist[(i,j)] = w[(i,j)]
                prev[(i,j)] = i
            else:
                dist[(i,j)] = float('inf')
                prev[(i,j)] = None

    for k in V:
        for i in V:
            for j in V:
                if dist[(i,j)] > dist[(i,k)] + dist[(k,j)]:
                    dist[(i,j)] = dist[(i,k)] + dist[(k,j)]
                    prev[(i,j)] = prev[(k,j)]

    return dist, prev
