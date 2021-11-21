def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent, ranks):
    root_u = find(u, parent)
    root_v = find(v, parent)
    if root_v == root_u:
        return
    if ranks[root_v] > ranks[root_u]:
        parent[root_u] = root_v
    elif ranks[root_u] > ranks[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_u] = root_v
        ranks[root_v] += 1


def solver():
    V = int(input())
    arr = []
    for i in range(V):
        x, y = map(int, input().split())
        arr.append((i, x, y))

    # make set
    parent = [i for i in range(V)]
    ranks = [0 for _ in range(V)]
    for i in range(V):
        for j in range(V):
            (v1, x1, y1) = arr[i]
            (v2, x2, y2) = arr[j]
            if x1 == x2 or y1 == y2:
                union(v1, v2,parent,ranks)
    for i in range(V): find(i, parent)#path compression
    components = {}
    for i in parent:
        if i not in components:
            components[i]=1
    print(len(components)-1)
solver()