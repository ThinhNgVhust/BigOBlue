import heapq

INF = 1e9


def Prim(case):
    input()
    V = int(input())
    Adj = {}
    for i in range(V):
        city1, city2, cost = map(str, input().split())
        cost = int(cost)
        if city1 not in Adj:
            Adj[city1] = {}
        if city2 not in Adj:
            Adj[city2] = {}
        if city2 not in Adj[city1]:
            Adj[city1][city2] = INF
        Adj[city1][city2] = min(Adj[city1][city2], cost)
        if city1 not in Adj[city2]:
            Adj[city2][city1] = INF
        Adj[city2][city1] = min(Adj[city2][city1], cost)
    n_components = 0
    visited = {}
    for v in Adj.keys():
        if v not in visited:
            n_components += 1
            frontier = [v]
            visited[v] = True
            while frontier:
                next = []
                for vertex in frontier:
                    for u in Adj[vertex]:
                        if u not in visited:
                            visited[u] = True
                            next.append(u)
                frontier = next
        if n_components > 1:
            print("Case {0}: Impossible".format(case))
            return

    distances = {}
    for key in Adj.keys():
        distances[key] = INF
    pq = [(0, city2)]
    visited = {}
    while pq:
        w,v = heapq.heappop(pq)
        if v in visited:continue
        visited[v] = True
        for u in Adj[v]:
            if u not in visited and distances[u]>Adj[v][u]:
                distances[u] = Adj[v][u]
                heapq.heappush(pq,(distances[u],u))
    total = 0
    for k in distances:
        if distances[k]!=INF:
            total+=distances[k]
    print("Case {0}: {1}".format(case,total))
    return


T = int(input())
for case in range(1, T + 1):
    Prim(case)
