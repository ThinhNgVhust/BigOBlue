import heapq


def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


maxVal = 1
minVal = 1


def union(u, v, parent, ranks, V, arr):
    global maxVal, minVal
    up = find(u, parent)
    vp = find(v, parent)
    if len(V) == 1:
        print(0)
        return
    if up == vp:
        print(maxVal - minVal)
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        V[up] += V[vp]
        maxVal = max(maxVal, V[up])
        heapq.heappush(arr, (V[up], up))
        # heapq.heappush(arr, (V[up], vp))
        del V[vp]
    elif ranks[vp] > ranks[up]:
        parent[up] = vp
        V[vp] += V[up]
        maxVal = max(maxVal, V[vp])
        heapq.heappush(arr, (V[vp], vp))
        del V[up]
    else:
        parent[up] = vp
        ranks[vp] += 1
        V[vp] += V[up]
        V[up] = 0
        maxVal = max(maxVal, V[vp])
        heapq.heappush(arr, (V[vp], vp))
        del V[up]

    while True:
        minVal, v = arr[0]
        if v in V and minVal == V[v]:
            break
        else:
            heapq.heappop(arr)

    print(maxVal - minVal)


def solver():
    N, Q = map(int, input().split())
    parent = [i for i in range(N)]
    ranks = [0 for i in range(N)]
    V = {}
    arr = []
    for i in range(N):
        V[i] = 1
        arr.append((1, i))
    for i in range(Q):
        u, v = map(int, input().split())
        union(u - 1, v - 1, parent, ranks, V, arr)


solver()
