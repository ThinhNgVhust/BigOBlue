INF = int(1e19)


def solver():
    while True:
        N = int(input())
        if N == 0:
            return
        DistYoung = [[INF for i in range(26)] for j in range(26)]
        DistMiguel = [[INF for i in range(26)] for j in range(26)]
        for i in range(26):
            DistYoung[i][i] = 0
            DistMiguel[i][i] = 0
        # print(DistMe)
        # print(DistMiguel)
        for i in range(N):
            arr = input().split()
            start = ord(arr[2]) - ord("A")
            end = ord(arr[3]) - ord("A")
            dis = int(arr[4])
            # print(arr[0])
            if arr[0] == "Y":  # young path
                if arr[1] == "U":  #
                    DistYoung[start][end] = min(DistYoung[start][end], dis)
                else:  # Bi-direction
                    DistYoung[start][end] = min(DistYoung[start][end], dis)
                    DistYoung[end][start] = min(DistYoung[end][start], dis)
            else:  # old path
                if arr[1] == "U":
                    DistMiguel[start][end] = min(DistMiguel[start][end], dis)
                else:  # Bi-direction
                    DistMiguel[start][end] = min(DistMiguel[start][end], dis)
                    DistMiguel[end][start] = min(DistMiguel[end][start], dis)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    DistYoung[i][j] = min(DistYoung[i][j], DistYoung[i][k] + DistYoung[k][j])
                    DistMiguel[i][j] = min(DistMiguel[i][j], DistMiguel[i][k] + DistMiguel[k][j])
        places = input().split()
        startMe = ord(places[0]) - ord("A")
        startMiguel = ord(places[1]) - ord("A")
        # print(DistYoung[startMe])
        # print(DistMiguel[startMiguel])
        minDis = INF
        for cite in range(26):
            if DistMiguel[startMiguel][cite] != INF and DistYoung[startMe][cite] != INF:
                minDis = min(DistMiguel[startMiguel][cite] + DistYoung[startMe][cite], minDis)

        if minDis == INF:
            print("You will never meet.")
        else:
            result = [str(minDis)]
            for cite in range(26):
                if minDis == DistMiguel[startMiguel][cite] + DistYoung[startMe][cite]:
                    result.append(chr(cite + ord("A")))
            print(" ".join(result))
solver()
