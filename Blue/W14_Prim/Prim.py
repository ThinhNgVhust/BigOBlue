import heapq

INF = 1e20


def prim():
    n, m = map(int, input().split())
    V = n
    Adj = [[] for i in range(V + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        Adj[u].append((v, w))
        Adj[v].append((u, w))
    dist = [INF for x in range(V + 1)]
    visited = [False for x in range(V + 1)]
    dist[0] = 0
    heap = [(0, 1)]
    while heap:
        w, v = heapq.heappop(heap)
        if visited[v] is True: continue
        visited[v] = True
        for u, w in Adj[v]:
            if visited[u] is False and dist[u] > w:
                dist[u] = w
                heapq.heappush(heap, (dist[u], u))
    sum = 0
    for e in dist:
        if e != INF:
            sum += e
    print(sum)


prim()
