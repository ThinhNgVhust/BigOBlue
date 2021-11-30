import sys

# sys.stdin = open('test1.txt', 'r')
sys.setrecursionlimit(1000000)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


INF = int(1e9)


def solver():
    usd_k, w, n = get_ints()
    total = int(n * (n + 1) / 2)
    total = total * usd_k
    if total <= w:
        print(0)
    else:
        print(total - w)


if __name__ == '__main__':
    solver()
