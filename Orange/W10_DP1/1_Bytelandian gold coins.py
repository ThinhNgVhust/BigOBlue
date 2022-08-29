import sys

def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline()


def read_all(): return sys.stdin.read()


def solve(n):
    if n in dict:
        return dict[n]
    else:
        if n // 2 not in dict: dict[n // 2] = solve(n // 2)
        if n // 3 not in dict: dict[n // 3] = solve(n // 3)
        if n // 4 not in dict: dict[n // 4] = solve(n // 4)
        dict[n] = max(n,dict[n//2] + dict[n//3]+dict[n//4])
        return dict[n]


dict = {}
for i in range(0, 12): dict[i] = i


def solver():
    arr = read_all().split()
    arr = [int(x) for x in arr]
    for e in arr:
        ans = solve(e)
        print(ans)


solver()
