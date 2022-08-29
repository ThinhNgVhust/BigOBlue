def convert(t):
    (h, m) = t.split(":")
    return int(h) * 60 + int(m)


if __name__ == "__main__":
    N = int(input())
    for test in range(N):
        T = int(input())
        (NA, NB) = map(int, input().split())
        trips = []
        for i in range(NA):
            (d, a) = input().split()
            trips.append((convert(d), convert(a), 0))
        for i in range(NB):
            (d, a) = input().split()
            trips.append((convert(d), convert(a), 1))
        trips.sort()
        res = [0, 0]
        pool = ([], [])
        for (d, a, t) in trips:
            if len(pool[t]) == 0 or pool[t][0] > d:
                res[t] += 1
            else:
                del pool[t][0]
            pool[1 - t].append(a + T)
            pool[1 - t].sort()
        print("Case #%d: %d %d" % (test + 1, res[0], res[1]))
