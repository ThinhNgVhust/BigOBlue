import heapq

INF = int(1e10)


def Prim(Adj):
    V = len(Adj)
    dist = [INF] * V
    visited = [False] * V
    path = [-1] * V
    for vertex in range(V):
        if visited[vertex] is False:
            hq = [(0, vertex)]
            while hq:
                _, v = heapq.heappop(hq)
                if visited[v] is True: continue
                visited[v] = True
                for u in Adj[v]:
                    if visited[u] is False and dist[u] > Adj[u][v]:
                        dist[u] = Adj[u][v]
                        path[u] = v
                        heapq.heappush(hq, (dist[u], u))
    return path, dist


def BFS(u, v, Adj):
    if u == v:
        return 0
    level = {u: 0}
    frontier = [u]
    visited = {u: True}
    while frontier:
        next = []
        for u in frontier:
            for u1 in Adj[u]:
                if u1 not in visited:
                    visited[u1] = True
                    next.append(u1)
                    level[u1] = max(Adj[u][u1], level[u])
                    if u1 == v:
                        return level[u1]
        frontier = next
    if v not in visited:
        return INF


def solver():
    case = 1
    while True:
        C, S, Q = map(int, input().split())
        if C == 0 and S == 0 and Q == 0:
            break
        Adj = {}
        for i in range(C): Adj[i] = {}
        for i in range(S):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            if v not in Adj[u]:
                Adj[u][v] = INF
            if u not in Adj[v]:
                Adj[v][u] = INF
            Adj[u][v] = min(Adj[u][v], w)
            Adj[v][u] = min(Adj[v][u], w)
        path, distances = Prim(Adj)
        Adj = {}
        for i in range(C):
            Adj[i] = {}
        for idx in range(len(path)):
            v1 = idx
            v2 = path[idx]
            if v2 != -1:
                Adj[v1][v2] = distances[idx]
                Adj[v2][v1] = distances[idx]
        print("Case #{0}".format(case))
        case += 1
        level = {}
        for query in range(Q):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            distance = INF
            if (u, v) in level:
                distance = level[(u, v)]
            else:
                distance = BFS(u, v, Adj)
                level[(u, v)] = distance
                level[(v, u)] = distance
            if distance == INF:
                print("no path")
            else:
                print(distance)
        print()


solver()
