def check_p_o_t(num):
    return num & (num - 1) == 0


def solver():
    T = int(input())
    for _ in range(T):
        n = input()
        arr = list(map(int, input().split()))
        for i in range(64):
            ans = 0xffffffff
            print(ans)


solver()
