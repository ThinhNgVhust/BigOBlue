def find(v, parent):
    if parent[v] < 0:
        return v
    else:
        parent[v] = find(parent[v],parent)
        return parent[v]


def union(x, y, parent):
    global Adj
    ux = find(x, parent)
    vy = find(y, parent)
    if ux == vy:
        return
    if parent[y] < parent[x]:
        x,y = y,x
    parent[x] +=parent[y]
    parent[y] = x


Adj = {}


def solver():
    n, q = map(int, input().split())
    # make set
    parent = [-1 for i in range(n)]
    global Adj
    for i in range(n): Adj[i] = 1
    for i in range(q):
        u,v = map(int,input().split())
        union(u-1,v-1,parent)
    ans = []
    for i in range(n):
        ans.append(str(find(i,parent)+1))
    print(" ".join(ans))
solver()