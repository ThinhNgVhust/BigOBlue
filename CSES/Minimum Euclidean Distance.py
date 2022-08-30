MIN = int(1e20)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


def distance(a, b):
    return int((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def update(a, b):
    global ans
    dis = distance(a, b)
    if dis < ans:
        ans = dis
    return


def combine(point_set, left, mid, right, min_dis):
    smallest = min_dis
    mid_point = point_set[mid]
    pt = []
    for i in range(left, right):
        if abs((point_set[i].x - mid_point.x) ** 2) < min_dis:
            pt.append(point_set[i])
    pt.sort(key=lambda x: x.y)
    for i in range(len(pt)):
        for j in range(i + 1, len(pt)):
            if (pt[i].y - pt[j].y) ** 2 >= min_dis:
                break
            smallest = min(smallest, distance(pt[i], pt[j]))
    return smallest


def rec(point_set, left, right):
    min_dis = MIN
    if right - left <= 3:
        for i in range(left, right):
            for j in range(i + 1, right):
                min_dis = min(min_dis, distance(point_set[i], point_set[j]))
        return min_dis
    mid = (left + right) >> 1
    min_dis = min(rec(point_set, left, mid), rec(point_set, mid, right))
    return min(min_dis, combine(point_set, left, mid, right, min_dis))


def solver():
    n = int(input())
    point_set = []
    for i in range(n):
        a, b = map(int, input().split())
        point_set.append(Point(a, b))
    point_set.sort(key=lambda point:point.x)
    ans = rec(point_set, 0, len(point_set))
    print(ans)


if __name__ == '__main__':
    solver()
