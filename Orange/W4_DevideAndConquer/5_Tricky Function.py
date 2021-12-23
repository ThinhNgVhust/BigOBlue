class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


def distance(A, B):
    return (A.x - B.x) ** 2 + (A.y - B.y) ** 2


def conquer(point_set, min_dis, mid):
    smallest = min_dis
    point_mid = point_set[mid]
    pt = []
    for point in point_set:
        if (point.x-point_mid.x)**2 <= min_dis:
            pt.append(point)
    pt.sort(key=lambda x: x.y)
    for i in range(len(pt)):
        for j in range(i+1,len(pt)):
            if (pt[i].y - pt[j].y)**2 >=min_dis:
                break
            smallest = min(smallest,distance(pt[i],pt[j]))
    return smallest
MIN = int(1e20)


def divide_and_conquer(point_set):
    min_dis = MIN
    if len(point_set) <= 3:
        n = len(point_set)
        for i in range(n):
            for j in range(i + 1, n):
                min_dis = min(min_dis, distance(point_set[i], point_set[j]))
        return min_dis
    mid = len(point_set) // 2
    left = point_set[:mid]
    right = point_set[mid + 1:]
    min_left_dis = divide_and_conquer(left)
    min_right_dis = divide_and_conquer(right)
    min_dis = min(min_left_dis, min_right_dis)
    merge_dis = conquer(point_set, min_dis, mid)
    return min(min_dis, merge_dis)


def solver():
    n = int(input())
    X = [int(x) for x in input().split()]
    Y = [X[0]]
    for i in range(1, len(X)):
        Y.append(X[i] + Y[-1])
    point_set = [None] * n
    for i in range(n):
        point_set[i] = Point(i, Y[i])
    point_set.sort(key=lambda point: point.x)
    ans = divide_and_conquer(point_set)
    print(ans)


solver()
