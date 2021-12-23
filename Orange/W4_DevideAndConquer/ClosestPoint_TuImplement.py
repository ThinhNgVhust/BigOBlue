class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


MIN = int(1e20)


def combine_sol(arr, left, right, mid, min_dis):
    mid_point = arr[mid]
    points_considering = []
    for i in range(left, right):
        if abs(arr[i].x - mid_point.x) <= min_dis:
            points_considering.append(arr[i])
    points_considering.sort(key=lambda point: point.y)
    l = len(points_considering)
    smallest = min_dis
    for i in range(l):
        for j in range(i + 1, l):
            if abs(points_considering[i].y - points_considering[j].y) <= min_dis:
                smallest = min(smallest, distance(arr[i], arr[j]))
    return smallest


def min_dis_brute_force(arr, left, right):
    min_dis = MIN
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dis = min(min_dis, distance(arr[i], arr[j]))
    return min_dis


def solver(arr, left, right):
    if right - left <= 3:
        return min_dis_brute_force(arr, left, right)
    mid = (right + left) // 2
    min_dis_left = solver(arr, left, mid)
    min_dis_right = solver(arr, mid + 1, right)
    min_dis = min(min_dis_left, min_dis_right)
    return min(min_dis, combine_sol(arr, left, right, mid, min_dis))


if __name__ == '__main__':
    arr = [[0, 2], [6, 67, ], [43, 71], [39, 107], [189, 140]]
    arr = [Point(x[0], x[1]) for x in arr]
    arr.sort(key=lambda point: point.x)
    print(solver(arr, 0, len(arr)))
