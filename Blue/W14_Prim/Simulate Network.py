import heapq

INF = int(1e20)


def Prim(Adj):
    V = len(Adj)
    visited = [False] * V
    dist = [INF] * V
    hq = [(0, 0)]
    while hq:
        _, v = heapq.heappop(hq)
        if visited[v] is True: continue
        visited[v] = True
        for u in Adj[v]:
            if visited[u] is False and dist[u] > Adj[v][u]:
                dist[u] = Adj[v][u]
                heapq.heappush(hq, (dist[u], u))
    return dist


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
    distances = Prim(Adj)
    distances[0], distances[-1] = distances[-1], distances[0]
    distances.pop()
    distances = [-x for x in distances]
    Q = int(input())
    arr = [int(x) for x in input().split()]
    heapq.heapify(distances)
    heapq.heapify(arr)
    while arr[0] < -distances[0]:
        old = -heapq.heappop(distances)
        new = heapq.heappop(arr)
        old = new
        heapq.heappush(distances, -old)
    s = 0
    for e in distances:
        s += e
    print(-s)


solver()
