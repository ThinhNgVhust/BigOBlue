import heapq


def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent, ranks):
    up = find(u, parent)
    vp = find(v, parent)
    if up == vp:
        return False
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1
    return True


import heapq


def kruskal(edges):
    # makeSet
    V = len(edges)
    parent = [i for i in range(V)]
    ranks = [0 for _ in range(V)]
    # edges is array of (w,u,v)
    sum_of_weight = 0
    heapq.heapify(edges)
    while edges:
        (w, v, u) = heapq.heappop(edges)
        if union(u, v, parent, ranks) is True:
            sum_of_weight += w
    return sum_of_weight


def solver():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))
    print(kruskal(edges))
    return
solver()
