def solver():
    test_case = int(input())
    for case in range(test_case):
        cnt = 0
        arr = input()
        V = len(arr)
        INF = int(1e50)
        dist = [[INF for i in range(V)] for j in range(V)]

        for i in range(len(arr)):
            if arr[i] == "Y":
                dist[cnt][i] = 1
                dist[i][cnt] = 1
        cnt += 1
        for h in range(V - 1):
            arr = input()
            for i in range(len(arr)):
                if arr[i] == "Y":
                    dist[cnt][i] = 1
                    dist[i][cnt] = 1
            cnt += 1
        for i in range(V): dist[i][i] = 0
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        result = [0]*V
        n =0
        for arr in dist:
            cnt = 0
            for i in arr:
                if i == 2:
                    cnt+=1
            result[n] = cnt
            n += 1
        # print(result)
        maxVal = -INF
        for e in result:
            if maxVal<e:
                maxVal = e
        for i in range(len(result)):
            if result[i] == maxVal:
                print(i,maxVal)
                break

solver()
