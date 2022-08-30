def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent, ranks):
    up = find(u, parent)
    vp = find(v, parent)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        ranks[up] += ranks[vp]
    elif ranks[up] <= ranks[vp]:
        parent[up] = vp
        ranks[vp] += ranks[up]


def solver():
    n, q = map(int, input().split())
    ranks = [1 for i in range(n)]
    parent = [i for i in range(n)]
    for i in range(q):
        querie = input().split()
        if len(querie) == 3:
            union(int(querie[1]) - 1, int(querie[2]) - 1, parent, ranks)
        else:
            print(ranks[find(int(querie[1]) - 1, parent)])


solver()
