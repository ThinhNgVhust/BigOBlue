INF = int(1e20)


def Floyd(Matrix, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                Matrix[i][j] = min(Matrix[i][j], max(Matrix[i][k], Matrix[k][j]))


def solver():
    case = 1
    while True:
        C, S, Q = map(int, input().split())
        if C == 0 and S == 0 and Q == 0:
            break
        Matrix = [[INF for i in range(C)] for j in range(C)]
        for i in range(C): Matrix[i][i] = 0
        for i in range(S):
            u, v, w = map(int, input().split())
            u -= 1
            v -= 1
            Matrix[u][v] = w
            Matrix[v][u] = w
        Floyd(Matrix, C)
        print("Case #{0}".format(case))
        case += 1
        for i in range(Q):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            distance = Matrix[u][v]
            if distance == INF:
                print("no path")
            else:
                print(distance)
        print()


solver()
