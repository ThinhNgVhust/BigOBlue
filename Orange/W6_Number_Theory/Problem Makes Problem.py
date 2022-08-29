import math


def cache(number, MOD):
    arr = [1]
    result = 1
    for i in range(1, 2 * number + 1):
        result = result * i
        result = result % MOD
        arr.append(result)
    return arr


def pow_mod(a, base, m):
    if base == 0:
        return 1
    t = pow_mod(a, base // 2, m)
    if base % 2 == 0:
        return (t * t) % m
    else:
        return (a * t * t) % m


def solver():
    MOD = 1000000007
    arr = cache(int(1e6), MOD)
    T = int(input())
    for case in range(1, T + 1):
        n, k = map(int, input().split())
        number = arr[k - 1] * arr[n]
        inverse = pow_mod(number, MOD - 2, MOD)
        ans = (arr[n + k - 1] * inverse) % MOD
        print("Case {}: {}".format(case, ans % MOD))


solver()
