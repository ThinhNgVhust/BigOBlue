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


import math


def solver():
    case = int(input())
    input()
    for T in range(case):
        m = int(input())
        pos = []
        for i in range(m):
            x, y = map(float, input().split())
            pos.append((x, y))
        edges = []
        for i in range(m):
            for j in range(m):
                if i == j: continue
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                w = (x2 - x1) ** 2 + (y2 - y1) ** 2
                w = math.sqrt(w)
                edges.append((w, i, j))
        sum = 0
        sum = kruskal(edges)
        print("{:.2f}".format(sum))
        if T != (case - 1):
            print()
            input()


solver()
