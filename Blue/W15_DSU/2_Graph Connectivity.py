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
    ends = False
    T = int(input())
    input()
    for _ in range(T):
        vertex = input()
        N = ord(vertex) - ord("A")+1
        Adj = {}
        for i in range(N):
            Adj[chr(ord("A") + i)] = i
        # make set
        parent = [i for i in range(N)]
        ranks = [0 for i in range(N)]
        while True:
            try:
                s = input()
                if len(s) == 0:
                    break
                vertex1, vertex2 = Adj[s[0]], Adj[s[1]]
                unionSet(vertex1, vertex2, parent, ranks)
            except EOFError as e:
                ends=True
                # print("True")
                break
        for k in Adj:
            findSet(Adj[k], parent)
        # find number of connected components
        arr_ans = [0] * N
        for idx in parent:
            arr_ans[parent[idx]] += 1
        ans = 0
        for e in arr_ans:
            if e!=0:
                ans+=1
        print(ans)
        if ends is False:
            print()


solver()
