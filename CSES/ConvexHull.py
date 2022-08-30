# using Graham algorithms
# Source:https://vnoi.info/wiki/translate/wcipeg/Convex-Hull.md#thu%E1%BA%ADt-to%C3%A1n-graham
EPS = 1e-10


class Point:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.id)

    def __str__(self):
        return "id = {}, ({} {})".format(self.id, self.x, self.y)


def cmp(a):
    if a.x == 0:
        return 0
    ans = (a.x-1) / abs(a.x)
    return ans


def length(vector):
    return (vector.x ** 2 + vector.y ** 2) ** 0.5


def ccw(point_a, point_b, point_c):  # tich có hướng giữa 3 điểm
    ab = Point(point_b.x - point_a.x, point_b.y - point_a.y)
    bc = Point(point_c.x - point_b.x, point_c.y - point_b.y)
    z = ab.x * bc.y - ab.y * bc.x
    if abs(z) < EPS:
        return 0
    if z < EPS:
        return -1
    return 1


if __name__ == '__main__':
    point_set = []
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        point_set.append(Point(x, y, i))
    min_h_point = point_set[0]
    for e in point_set:
        if min_h_point.y > e.y:
            min_h_point = e
    point_set = [(e - min_h_point) for e in point_set]
    origin = point_set[0]
    I = point_set[1]
    # point_set = point_set[1:]
    point_set.sort(key=cmp)
    for e in point_set:
        print(e)
    stack = []
    stack.append(origin)
    stack.append()