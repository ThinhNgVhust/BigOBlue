import heapq
import sys

INF = int(1e9)


# sys.stdin = open('test1.txt', 'r')
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def solver():
    while True:
        N, M = get_ints()
        if N == 0 and M == 0:
            return
        S, D = get_ints()

        Adj = {}
        for i in range(N):
            Adj[i] = {}

        for _ in range(M):
            U, V, P = get_ints()
            Adj[U][V] = P
        dijsktra(Adj, S, D)


def dijsktra(Adj, start, end):
    distance = [INF] * len(Adj)
    parent = {}
    distance[start] = 0
    stack = [(distance[start], start)]
    while stack:
        (w, v) = heapq.heappop(stack)
        if distance[v] != w: continue
        for u in Adj[v].keys():
            cost = Adj[v][u]
            if distance[u] > distance[v] + cost:
                distance[u] = distance[v] + cost
                heapq.heappush(stack, (distance[u], u))
                if u in parent:
                    del parent[u]
                parent[u] = [v]
            elif distance[u] == distance[v] + cost:
                parent[u].append(v)
    if distance[end] == INF:
        print("-1")
        return
    # delete path from shortest path
    stack = [end]
    while stack:
        target = stack.pop()
        if target in parent:
            for source in parent[target]:
                if source in Adj and target in Adj[source]:
                    del Adj[source][target]
                    stack.append(source)

    distance = [INF] * len(Adj)
    parent = {}
    distance[start] = 0
    stack = [(distance[start], start)]
    while stack:
        (w, v) = heapq.heappop(stack)
        if distance[v] != w: continue
        for u in Adj[v].keys():
            cost = Adj[v][u]
            if distance[u] > distance[v] + cost:
                distance[u] = distance[v] + cost
                heapq.heappush(stack, (distance[u], u))
                if u in parent:
                    del parent[u]
                parent[u] = [v]
            elif distance[u] == distance[v] + cost:
                parent[u].append(v)
    if distance[end] == INF:
        print("-1")
    else:
        print(distance[end])


if __name__ == '__main__':
    solver()
