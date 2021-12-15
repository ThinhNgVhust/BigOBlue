def findSet(u, parent):
    if u != parent[u]:
        parent[u] = findSet(parent[u], parent)
    return parent[u]


def unionSet(u, v, parent, ranks):
    # path compression
    up = findSet(u, parent)
    vp = findSet(v, parent)
    if up == vp: return
    # union by rank
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:  # bang nhau noi kieu gi cung duoc
        parent[up] = vp
        ranks[vp] += 1
    findSet(u, parent)
    findSet(v, parent)


def solver():
    T = int(input())
    for case in range(T):
        N = int(input())
        parent = [i for i in range(N)]
        ranks = [0 for i in range(N)]
        n_components = {}
        E = int(input())
        for i in range(E):
            a, b = map(int, input().split())
            unionSet(a, b, parent, ranks)
        for i in range(N):
            findSet(i, parent)
            n_components[parent[i]] = 1
        print(len(n_components))


solver()
