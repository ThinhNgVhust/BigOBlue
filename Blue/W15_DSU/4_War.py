def findSet(u, parent):
    if u != parent[u]:
        parent[u] = findSet(parent[u], parent)
    return parent[u]


def unionSet(u, v, parent, ranks):
    up = findSet(u, parent)
    vp = findSet(v, parent)
    if up == vp:
        return 0
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
    else:
        parent[vp] = up
        ranks[up] += 1
    return 1


def solver():
    N = int(input())
    Adj = {}
    friends = [i for i in range(2*N)]
    ranks_friends = [0 for _ in range(2*N)]
    while True:
        c, x, y = map(int, input().split())
        if x == 0 and y == 0 and c == 0: break
        if c == 1:
            # set friend x,y
            f_x = findSet(x, friends)
            f_y = findSet(y, friends)
            e_x = findSet(x+N, friends)
            e_y = findSet(y+N, friends)
            if f_x == e_y or f_y == e_x:
                print("-1")
            else:
                unionSet(e_x, e_y,friends,ranks_friends)
                unionSet(f_x, f_y,friends,ranks_friends)
        elif c == 2:
            # set enemie
            f_x = findSet(x, friends)
            f_y = findSet(y, friends)
            e_x = findSet(x+N, friends)
            e_y = findSet(y+N, friends)
            if f_x == f_y or e_x == e_y:
                print("-1")
            else:
                unionSet(f_x,e_y,friends,ranks_friends)
                unionSet(f_y,e_x,friends,ranks_friends)
        elif c == 3:
            #areFriend
            if findSet(x,friends)==findSet(y,friends):
                print("1")
            else:
                print("0")
        elif c == 4:
            if findSet(x,friends) == findSet(y+N,friends):
                print("1")
            else:
                print("0")


solver()
