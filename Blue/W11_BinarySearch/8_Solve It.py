from bisect import bisect_left, bisect_right

import math

import sys

INF = int(1e9)

sys.stdin = open('test.txt', 'r')


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def sin(x): return math.sin(x)


def cos(x): return math.cos(x)


def tan(x): return math.sin(x) / math.cos(x)


def exp(x): return math.exp(x)


epsilon = (1e-4)


def QPrime(x, p, q, r, s, t, u):
    return -x * p * exp(-x) + q * cos(x) - r * sin(x) + s / (cos(x)) ** 2 + t * 2 * x


def Q(x, p, q, r, s, t, u):
    return p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x ** 2 + u


def solver():
    while True:
        try:
            p, q, r, s, t, u = get_ints()
            left = 0.
            right = 1.
            has_no = False
            for i in range(25):
                x = (left+right)//2
                F = Q(x,p, q, r, s, t, u)
                if F>0:
                    left = x
                else:
                    right = x

        except:
            break


if __name__ == '__main__':
    solver()

