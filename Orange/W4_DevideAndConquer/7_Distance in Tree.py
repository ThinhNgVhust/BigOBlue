# f[u][dist] = f_s[u][dist] + (f[parent[u]][dist-1]-f_s[u][dist-2])
# f_s[u][0]=1
# f[root][0]=1
# f[i][0]=1
# f[root][dist]=f_sub[root][dist] for i in range(k+1)
# ans = tong f[i][dist] for i in range(0,N):
# ans/2 chinh la dap an
# tham khao goi y:https://codeforces.com/blog/entry/76080?#comment-604916
# sol nay dc AC neu viet bang C++, tren python se bi TLE hoac MLE
import sys

sys.setrecursionlimit(500000)
topo = []


def cal_f_sub(root, p, parent, Adj, f_sub, distance):
    f_sub[root][0] = 1  # co duy nhat chinh root co kc toi no la 0
    parent[root] = p
    for v in Adj[root]:
        if v not in parent:
            cal_f_sub(v, root, parent, Adj, f_sub, distance)
            for i in range(1, distance + 1):
                f_sub[root][i] += f_sub[v][i - 1]
    # print("Done visited ",root)
    topo.append(root)


def solver():
    import time
    start = time.time()
    # n, dist = map(int, input().split())
    n = 50000
    dist = 500
    Adj = {}
    for i in range(n): Adj[i] = []
    for i in range(n - 1):
        # a, b = map(lambda x: int(x) - 1, input().split())
        Adj[i].append(i + 1)
        Adj[i + 1].append(i)
    root = 0
    f_sub = [[0 for i in range(dist + 1)] for j in range(n)]  # 0 1 2 3 .... k
    parent = {}
    # print("thinh")
    cal_f_sub(root, None, parent, Adj, f_sub, dist)
    # print(f_sub)
    topo.reverse()
    # print(topo)
    f = [[0 for i in range(dist + 1)] for j in range(n)]
    f[root][0] = 1
    for i in range(dist + 1):
        f[root][i] = f_sub[root][i]
    for i in range(n):
        f[i][0] = 1
    for idx in range(1, len(topo)):
        u = topo[idx]
        for i in range(1, dist + 1):
            if i >= 2:
                f[u][i] = f_sub[u][i] + (f[parent[u]][i - 1] - f_sub[u][i - 2])
            else:
                f[u][i] = f_sub[u][i] + (f[parent[u]][i - 1])
    end = time.time()

    ans = 0
    for i in range(n):
        ans += f[i][dist]
    print(ans // 2)
    print(start - end)


solver()
