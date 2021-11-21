def findSet(u, parent):
    # path compression
    if u != parent[u]:
        parent[u] = findSet(parent[u], parent)
    return parent[u]


def unionSet(u, v, parent, ranks):
    # using union by rank
    up = findSet(u, parent)
    vp = findSet(v, parent)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
    else:
        parent[vp] = up
        ranks[up] += 1

def solver():
    case = 1
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            return
        parent = [i for i in range(n)]
        ranks = [0 for i in range(n)]
        for i in range(m):
            u,v = map(lambda x:int(x)-1,input().split())
            unionSet(u,v,parent,ranks)
        for i in range(n):findSet(i,parent)
        Adj = {}
        for i in range(n):Adj[parent[i]] = True
        print("Case {0}: {1}".format(case,len(Adj)))
        case+=1

if __name__ == '__main__':
    solver()