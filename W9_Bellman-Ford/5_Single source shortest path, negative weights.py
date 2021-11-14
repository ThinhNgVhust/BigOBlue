import heapq
import sys

INF = int(1e9)


# sys.stdin = open('test1.txt', 'r')
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()

def BellmanFord(Adj,dis,s,V):
    dis[s] = 0
    for _ in range(V-1):
        flag = False
        for edge in Adj:
            source,des,weight = edge[0],edge[1],edge[2]
            if dis[source]!=INF and dis[source] +weight < dis[des]:
                dis[des] = dis[source]  +weight
                flag = True
        if flag is False:
            break
    for _ in range(V):
        for edge in Adj:
            source, des, weight = edge[0], edge[1], edge[2]
            if dis[source] != INF and dis[des] > dis[source] + weight:
                dis[des] = -INF

def solver():
    while True:
        n, m, q, s = get_ints()
        if n == 0 and m == 0 and q == 0 and s == 0:
            return
        Adj = []
        V = n
        for _ in range(m):
            u, v, w = get_ints()
            Adj.append((u,v,w))
        dis = [INF]*V
        BellmanFord(Adj,dis,s,V)
        for _ in range(q):
            v =int(input())
            if dis[v] == INF:print("Impossible")
            elif dis[v] == -INF:print("-Infinity")
            else:print(dis[v])
        print()


if __name__ == '__main__':
    solver()