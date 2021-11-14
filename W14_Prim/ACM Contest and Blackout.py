import heapq

INF = int(1e9)


def Prim(Adj):
    dist = [INF] * len(Adj)
    path = [-1] * len(Adj)
    visited = [False] * len(Adj)
    stack = [(0, 0)]
    while stack:
        _, v = heapq.heappop(stack)
        if visited[v] is True: continue
        visited[v] = True
        for u in Adj[v].keys():
            if visited[u] is False and dist[u] > Adj[v][u]:
                dist[u] = Adj[v][u]
                heapq.heappush(stack, (dist[u], u))
                path[u] = v
    total = 0
    for e in dist:
        if e != INF:
            total += e
    return total, path


def Prim1(Adj):
    dist = [INF] * len(Adj)
    path = [-1] * len(Adj)
    visited = [False] * len(Adj)
    stack = [(0, 0)]
    dist[0] = 0
    while stack:
        _, v = heapq.heappop(stack)
        if visited[v] is True: continue
        visited[v] = True
        for u in Adj[v].keys():
            if visited[u] is False and dist[u] > Adj[v][u]:
                dist[u] = Adj[v][u]
                heapq.heappush(stack, (dist[u], u))
                path[u] = v
    total = 0
    for e in dist:
        if e != INF:
            total += e
        else:
            return -1
    return total


def solver():
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        Adj = {}
        for i in range(V): Adj[i] = {}
        for i in range(E):
            u, v, w = map(int, input().split())
            Adj[u - 1][v - 1] = w
            Adj[v - 1][u - 1] = w
        first, path = Prim(Adj)
        second = INF
        for i in range(len(path)):
            u = i
            v = path[i]
            if v != -1:
                w = Adj[u][v]
                Adj[u][v] = INF
                Adj[v][u] = INF
                temp = Prim1(Adj)
                if temp != -1:
                    second = min(temp, second)
                Adj[u][v] = w
                Adj[v][u] = w
        if second == INF:
            print(first, first)
        else:
            print(first, second)


solver()
