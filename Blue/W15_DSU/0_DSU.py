MAX = 20
parent = []
ranks = []


def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]


def findSet(u):
    # path compression
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    #union by rank
    up = findSet(u)
    vp = findSet(v)
    if up == vp: return

    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:  # bang nhau noi kieu gi cung duoc
        parent[up] = vp
        ranks[vp] += 1
    findSet(u)
    findSet(v)