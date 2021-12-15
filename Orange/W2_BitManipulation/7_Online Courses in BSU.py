import sys
sys.setrecursionlimit(int(1e5)+10)
has_cirlce = False


def solver():
    n, k = map(int, input().split())
    requires_course = list(map(lambda x: int(x), input().split()))
    Adj = {}
    for i in range(n): Adj[i + 1] = []
    for i in range(1, n + 1):
        datas = input()
        if len(datas) > 1:
            datas = list(map(lambda x: int(x), datas.split(" ")))
            Adj[i] = datas[1:].copy()
    parent = {}
    order = []
    circle = [0] * (n + 10)
    for vertex in requires_course:
        if vertex not in parent:
            dfs(vertex, Adj, parent, order, circle)
    global has_cirlce
    if has_cirlce:
        print("-1")
    else:
        print(len(order))
        print(" ".join([str(x) for x in order]))


def dfs(v, Adj, parent, orde, circle):
    global has_cirlce;
    parent[v] = True
    circle[v] = 1
    for u in Adj[v]:
        if u not in parent:
            dfs(u, Adj, parent, orde, circle)
        elif circle[u] == 1:
            has_cirlce = True
    circle[v] = 0
    orde.append(v)


solver()
