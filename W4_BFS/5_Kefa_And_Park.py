'''
Link:
Time complexity:
Space complexity:
'''
def solver():
    N, M = map(int, input().split())

    cats = [int(x) for x in input().split(" ")]
    Adj = {}

    for i in range(N - 1):
        u_v = [int(x) for x in input().split(" ")]
        if u_v[0] not in Adj:
            Adj[u_v[0]] = []
        Adj[u_v[0]].append(u_v[1])
        if u_v[1] not in Adj:
            Adj[u_v[1]] = []
        Adj[u_v[1]].append(u_v[0])
    level = {1: cats[0]}
    frontier = [1]
    result = []
    while frontier:
        next = []
        for v in frontier:
            for v1 in Adj[v]:
                if v1 not in level:
                    next.append(v1)
                    if cats[v1 - 1] == 1:
                        level[v1] = level[v] + cats[v1 - 1]
                    else:
                        level[v1] = 0
                    if len(Adj[v1]) == 1:  # leaf
                        if level[v1] <= M:
                            result.append(v1)
                    else:
                        if level[v1] > M:
                            next.pop()

        frontier = next
    print(len(result))


if __name__ == '__main__':
    solver()
