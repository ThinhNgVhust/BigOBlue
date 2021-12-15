def check(num):
    return num > 0 and (num & (num - 1) == 0)


def solve_one():
    input()
    arr = list(map(int, input().split()))
    for i in range(32):
        ans = 0xffffffff
        for e in arr:
            if e & (1 << i) != 0:
                ans = ans & e
                if check(ans) is True:
                    print("YES")
                    return
    print("NO")


def solver():
    T = int(input())
    for _ in range(T):
        solve_one()


solver()
