import heapq

INF = int(2 ** 32)


def Prim(Adj, source):
    V = len(Adj)
    dist = [INF] * V
    visited = [False] * V
    dist[source] = 0
    heap_arr = [(0, source)]
    while heap_arr:
        _, v = heapq.heappop(heap_arr)
        if visited[v] is True: continue
        visited[v] = True
        for u in Adj[v]:
            if visited[u] is False and dist[u] > Adj[u][v]:
                dist[u] = Adj[u][v]
                heapq.heappush(heap_arr, (dist[u], u))
    total = 0
    for e in dist:
        if e!=INF:
            total += e
    return total


def solver():
    N, M = map(int, input().split())
    Adj = {}
    for i in range(N): Adj[i] = {}
    for i in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        if v not in Adj[u]:
            Adj[u][v] = INF
        if u not in Adj[v]:
            Adj[v][u] = INF
        Adj[u][v] = min(Adj[u][v], w)
        Adj[v][u] = min(Adj[v][u], w)
    source = int(input())
    result = Prim(Adj, source - 1)
    print(result)


solver()
