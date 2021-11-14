INF = int(1e19)


def solver():
    case = 1
    while True:
        V = int(input())
        if V == 0:
            break
        ExchangeDict = {}

        for i in range(V):
            ExchangeDict[input()] = i
        M = int(input())
        dist = [[0 for i in range(V)] for i in range(V)]
        for i in range(V): dist[i][i] = 1.0
        for i in range(M):
            arr = input().split()
            start = arr[0]
            end = arr[2]
            value = float(arr[1])
            if start != end:
                dist[ExchangeDict[start]][ExchangeDict[end]] = value
                # dist[ExchangeDict[end]][ExchangeDict[start]] = 1./value

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if i <= k <= j:
                        dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])
        flag = "No"
        for i in range(V):
            if dist[i][i] > 1: flag = "Yes"
        print("Case {0}: {1}".format(case, flag))
        case += 1
        input()


solver()
