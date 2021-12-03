import sys
from collections import deque

# sys.stdin = open('test1.txt', 'r')
sys.setrecursionlimit(1000000)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


INF = int(1e9)


def solver():
    n, m = get_ints()
    arr = get_array()
    dq = deque(arr)
    ans = 0
    if len(arr) == 1:
        print(1)
        return
    while True :
        m -= 1
        element = dq.popleft()
        ck1 = False
        for i in range(len(dq)):
            if element < dq[i]:
                ck1 = True
                break
        if ck1 is False:
            ans += 1
            if m == -1:
                print(ans)
                return
        else:
            dq.append(element)
            if m == -1: m = len(dq) - 1
    # print(ans)


if __name__ == '__main__':
    n_test = int(input())
    for _ in range(n_test):
        solver()
