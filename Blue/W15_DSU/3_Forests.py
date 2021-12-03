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
        P, T = map(int, input().split())
        # make set
        parent = [i for i in range(P)]
        ranks = [0 for i in range(P)]
        Adj_tree = {}
        for i in range(P):
            Adj_tree[i] = []
        while True:
            try:
                s = input()
                if len(s) == 0:
                    break
                arr = [int(x) - 1 for x in s.split()]
                person, tree = arr[0], arr[1]
                if tree not in Adj_tree[person]:
                    Adj_tree[person].append(tree)
            except EOFError as e:
                ends = True
                # print("True")
                break
        for k in Adj_tree:
            Adj_tree[k].sort()
        # find number of connected components
        for i in range(P):
            for j in range(P):
                if i != j:
                    if Adj_tree[i] == Adj_tree[j]:
                        unionSet(i, j, parent, ranks)
        for i in range(P): findSet(i, parent)
        arr_ans = [0]*P
        for idx in range(len(parent)):
            arr_ans[parent[idx]]+=1
        ans = 0
        for e in arr_ans:
            if e!=0:ans+=1
        print(ans)
        if ends is False:
            print()
solver()

