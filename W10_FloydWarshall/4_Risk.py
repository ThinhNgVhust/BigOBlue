INF = float("inf")


def get_array(): return list(map(int, input().split()))


def get_ints(): return map(int, input().split())


def Floyd(dist):
    for k in range(1,21):
        for i in range(1,21):
            for j in range(1,21):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def solver():
    T = 1
    while True:
        try:
            Adj = {}
            dist = [[INF for i in range(21)] for j in range(21)]
            for i in range(1,20):
                s = input()
                if len(s) != 1:
                    arr = list(map(int, s.split()))
                    for e in arr[1:]:
                        dist[i][e] = 1
                        dist[e][i] = 1
            q = int(input())
            for i in range(1,21): dist[i][i] = 0
            Floyd(dist)
            print("Test Set #{0}".format(T))
            T += 1
            for _ in range(q):
                u, v = get_ints()
                distance = dist[v][u]
                if u<10: u = " "+str(u)
                if v<10:v = " "+str(v)
                print("{0} to {1}: {2}".format(u,v,distance))
            print()
        except EOFError as e:
            break


solver()
