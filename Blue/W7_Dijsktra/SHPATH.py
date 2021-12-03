import heapq

INF = int(1e9)
MAX = 10000 + 1


class Vertex:
    def __init__(self, label, dis):
        self.label = label
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis


def solver():
    Adj = {}
    cites = {}
    n = int(input())
    for i in range(n):
        vertex = i + 1
        Adj[vertex] = {}
        name = input()
        cites[name] = i + 1
        n = int(input())
        for _ in range(n):
            u, w = map(int, input().split())
            Adj[vertex][u] = w
    r = int(input())
    for _ in range(r):
        city1, city2 = input().split()
        vertex1, vertex2 = cites[city1], cites[city2]
        dijsktra(vertex1, vertex2, Adj)


import heapq

path = {}


def dijsktra(vertex1, vertex2, Adj):
    # if vertex1 in path:
    #     if vertex2 in path[vertex1]:
    #         print(path[vertex1][vertex2])
    #         return
    dis = [INF] * MAX
    dis[vertex1] = 0
    visited = [False] * MAX
    stack = [(dis[0], vertex1)]
    while stack:
        vertex = heapq.heappop(stack)
        v = vertex[1]
        if visited[v]:
            continue
        if v == vertex2:
            break
        for u in Adj[v].keys():
            if not visited[u]:
                if dis[u] > dis[v] + Adj[v][u]:
                    dis[u] = dis[v] + Adj[v][u]
                    heapq.heappush(stack, (dis[u], u))

        visited[v] = True
    print(dis[vertex2])
    # if vertex2 not in path:
    #     path[vertex2] ={}
    # if vertex1 not in path:
    #     path[vertex1] = {}
    # path[vertex2][vertex1] =dis[vertex2]
    # path[vertex1][vertex2] =  dis[vertex2]


if __name__ == '__main__':
    test_case = int(input())
    for test in range(test_case):
        solver()
        if test != test_case - 1:
            input()
