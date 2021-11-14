def solver():
    n = int(input())
    if n == 1:
        print(0)
    else:
        V = n
        Matrix = []
        for i in range(V):
            arr = list(map(int, input().split()))
            Matrix.append(arr)
        arr = list(map(int, input().split()))
        arr.reverse()
        ans = []
        visited = [False] * V

        def Floyd(dist, arr):
            for k in arr:
                ans.append(0)
                k -= 1
                visited[k] = True
                for i in range(V):
                    for j in range(V):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        if visited[i] is True and visited[j] is True: ans[-1] += dist[i][j]

        Floyd(Matrix, arr)
        ans.reverse()
        print(" ".join([str(x) for x in ans]))


solver()
