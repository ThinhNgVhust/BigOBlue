from math import frexp

INF = int(1e9)


def bfs(Adj, start, end):
    N = len(Adj)
    visited = [False] * N
    dis = [0] * N
    visited[start] = True
    frontier = [start]
    while frontier:
        next = []
        for v in frontier:
            for u in Adj[v]:
                if not visited[u]:
                    dis[u] = dis[v] + 1
                    visited[u] = True
                    next.append(u)
        frontier = next
    visited = [False] * N
    dis1 = [0] * N
    frontier = [end]
    visited[end] = True
    while frontier:
        next = []
        for v in frontier:
            for u in Adj[v]:
                if not visited[u]:
                    dis1[u] = dis1[v] + 1
                    visited[u] = True
                    next.append(u)
        frontier = next
    return max([x + y for x, y in zip(dis, dis1)])


def solver(case):
    N = int(input())
    R = int(input())
    Adj = {}
    for i in range(N): Adj[i] = []
    for j in range(R):
        u, v = map(int, input().split())
        Adj[u].append(v)
        Adj[v].append(u)
    s, d = map(int, input().split())

    distance = bfs(Adj, s, d)
    print("Case {0}: {1}".format(case, distance))


if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        solver(case + 1)
