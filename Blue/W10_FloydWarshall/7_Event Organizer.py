MAX = 49
INF = int(2 ** 64)


def solver():
    T = int(input())
    for _ in range(T):
        solve_one()


def solve_one():
    m = int(input())
    dist = [[0 for i in range(MAX)] for j in range(MAX)]
    for i in range(m):
        start, end, pay = map(int, input().split())
        dist[start][end ] = max(pay, dist[start][end])
    for k in range(MAX):
        for i in range(MAX):
            for j in range(MAX):
                if i <= k <= j:
                    dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(len(dist)):
        arr = dist[i]
        for e in arr:
            ans = max(ans,e)
    print(ans)


solver()
