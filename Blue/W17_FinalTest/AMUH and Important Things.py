import math


def method1():
    T = int(input())
    for i in range(1, T + 1):
        x = int(input())
        root = math.ceil(math.sqrt(x))
        lackings = root * root - x
        col = 0
        row = 0
        if lackings < root:
            row = root
            col = lackings + 1
        else:
            col = root
            row = x - (root - 1) * (root - 1)
        if root % 2 == 0:
            col, row = row, col
        print("Case {0}: {1} {2}".format(i, col, row))


method1()