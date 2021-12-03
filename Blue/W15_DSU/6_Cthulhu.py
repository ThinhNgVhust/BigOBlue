def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


circle = 0


def union(u, v, parent, ranks):
    up = find(u, parent)
    vp = find(v, parent)
    global circle
    if up == vp:
        circle += 1
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


def solver():
    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    global circle
    for i in range(M):
        u, v = map(int, input().split())
        union(u - 1, v - 1, parent, ranks)
    for i in range(N):
        find(i, parent)
    Adj = {}  # dem so thanh phan lien thong
    for e in parent:
        Adj[e] = True
    if len(Adj) > 1:  # neu nhieu hon 1 thanh phan lien thong
        print("NO")
        return
    if circle == 1:
        print("FHTAGN!")
        # return
    else:
        print("NO")
    # return


solver()
