import math

INF = int(1e19)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def bruteForce(arr, left, right):
    min_dis = INF
    for i in range(left, right):
        pt1 = arr[i]
        for j in range(i + 1, right):
            pt2 = arr[j]
            min_dis = min(min_dis, distance(pt1, pt2))
    return min_dis


def stripClosest(point_set, left, right, mid, min_dis):
    point_mid = point_set[mid]
    pt = []
    for i in range(left, right):
        p = point_set[i]
        if abs(p.x - point_mid.x) <= min_dis:
            pt.append(p)
    pt.sort(key=lambda pt:pt.y)#move to brute force
    smallest = min_dis
    l = len(pt)
    for i in range(l):
        for j in range(i + 1, l):
            if not (pt[i].y - pt[j].y) < smallest: break
            smallest = min(smallest, distance(pt[i], pt[j]))
    return smallest


def minimun_distance(point_set, left, right):
    if right - left <= 3:#base
        return bruteForce(point_set, left, right)
    mid = (right + left) // 2
    min_dist_left = minimun_distance(point_set, left, mid)#divide left
    min_dist_right = minimun_distance(point_set, mid + 1, right)#devide right
    min_dis = min(min_dist_left, min_dist_right)
    return min(min_dis, stripClosest(point_set, left, right, mid, min_dis))#combine


def solver():
    while True:
        N = int(input())
        if N == 0:
            return
        arr = []
        for i in range(N):
            x, y = map(int, input().split())
            arr.append(Point(x, y))
        arr.sort(key=lambda p: p.x)
        ans = minimun_distance(arr, 0, len(arr))
        if ans>=10000:
            print("INFINITY")
        else:
            print("{:.4f}".format(round(ans, 4)))


solver()