import heapq

INF = 2 ** 32


def Prim():
    p = int(input())
    n = int(input())
    m = int(input())
    Adj = {}
    V = n
    for i in range(V): Adj[i + 1] = {}
    for i in range(m):
        u, v, w = map(int, input().split())
        if v not in Adj[u]:
            Adj[u][v] = INF
        if u not in Adj[v]:
            Adj[v][u] = INF
        Adj[u][v] = min(Adj[u][v], w)
        Adj[v][u] = min(Adj[v][u], w)
    visited = {}
    dist = [INF for i in range(V + 1)]
    hq = [(0, 1)]
    while hq:
        w, v = heapq.heappop(hq)
        if v in visited: continue
        visited[v] = True
        for u in Adj[v]:
            if u not in visited and dist[u] > Adj[v][u]:
                dist[u] = Adj[v][u]
                heapq.heappush(hq,(dist[u],u))
    total = 0
    for e in dist:
        if e!=INF:
            total+=e
    print(total*p)
    pass


n_test = int(input())
for i in range(n_test):
    Prim()
