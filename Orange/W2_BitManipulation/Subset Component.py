def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent, ranks):
    up = find(u, parent)
    vp = find(v, parent)
    if up != vp:
        if up > vp:
            parent[vp] = up
        elif up < vp:
            parent[up] = vp
        else:
            parent[up] = vp
            ranks[vp] += 1


def count_components(i, prev_components, cliques):
    n = 1 << len(cliques)# so cac subset
    ans = 0
    for i in range(n):#duyet tung subset
        idx = []
        for j in range(0,64):
            if 1 << j & i != 0: idx.append(j)
        sub_Set =[cliques[i] for i in idx]#lay nhung subset
        parent = [i for i in range(64)]
        ranks = [0 for i in range(64)]
        Adj = {}
        for e in sub_Set:
            cnt =[]
            for k in range(64):
                if 1<<k &e!=0:cnt.append(k)
            if len(cnt)>1:
                for i in range(len(cnt)):
                    union(cnt[0],cnt[i],parent,ranks)
        for i in range(64):
                Adj[find(i,parent)]=1
        ans+=len(Adj)
    return ans


if __name__ == '__main__':
    n = int(input().strip())
    d = input().strip().split()
    d = [int(v) for v in d]
    assert len(d) == n

    singletons = [1 << j for j in range(64)]
    print(count_components(0, singletons, d))
