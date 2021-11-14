import heapq
import sys

INF = int(1e9)


#sys.stdin = open('test1.txt', 'r')
def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def BellmanFord(Adj, dis, source,n):
    dis[source] = 0
    V = n
    for _ in range(1, V):
        flag = False
        for edge in Adj:
            source, des, weight = edge[0], edge[1], edge[2]
            if dis[source] != INF and dis[des] > dis[source] + weight:
                dis[des] = dis[source] + weight
                flag = True
        if flag == False: break
    for i in range(V):
        for edge in Adj:
            source, des, weight = edge[0], edge[1], edge[2]
            if dis[source] != INF and dis[des] > dis[source] + weight:
                dis[des] = -INF



def solver(case):
    n = int(input())
    cost = get_array()
    Adj = []
    m = int(input())
    for i in range(m):
        u, v = get_ints()
        w = (cost[v-1] - cost[u-1]) ** 3
        Adj.append((u, v, w))
    dis = [INF] * (n + 1)

    BellmanFord(Adj, dis, 1,n)
    q = int(input())
    request = []
    print("Case {0}:".format(case))
    for _ in range(q):
        v = int(input())
        distance = dis[v]
        if distance == INF or distance == -INF or distance < 3:
            print("?")
        else:
            print(distance)


if __name__ == '__main__':
    n_test = int(input())
    for i in range(n_test):
        # if i !=n_test-1:
        input()
        solver(i + 1)
