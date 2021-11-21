MAX = 30000
parent = []
ranks = []
max_level = 0

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]


def findSet(u, parent, ranks,level = 0):
    global max_level
    max_level = max(max_level,level)
    # path compressionprint("level":level)
    if parent[u] != u:
        parent[u] = findSet(parent[u], parent, ranks,level+1)
    return parent[u]


def unionSet(u, v, parent, ranks):
    # Smaller to Larger
    up = findSet(u, parent, ranks)
    vp = findSet(v, parent, ranks)
    if up == vp: return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[vp] = up
    else:  # bang nhau noi kieu gi cung duoc
        parent[up] = vp
        ranks[vp] += 1


def solver():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        parent = [i for i in range(N)]
        ranks = [0 for i in range(N)]
        for i in range(M):
            u, v = map(int, input().split())
            unionSet(u-1, v-1, parent, ranks)
        ans = 0
        max_arr = [0]*(N)
        for i in range(N):findSet(i,parent,ranks)
        for i in range(len(parent)):
            if parent[i]!=i:
                max_arr[parent[i]]+=1
        ans = max(max_arr)
        print(ans+1)
solver()

