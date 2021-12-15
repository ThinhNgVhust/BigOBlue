def solver():
    n = int(input())
    arr = list(map(int, input().split()))
    XOR = [0] * (n + 1)
    cnt_0 = [0] * (n + 1)
    for i in range(1, len(arr)+1):
        XOR[i] = arr[i - 1] ^ XOR[i - 1]
        val = 1 - arr[i-1]
        cnt_0[i] = val + cnt_0[i - 1]
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        print((XOR[R] ^ XOR[L - 1]), (cnt_0[R] - cnt_0[L - 1]))

def solver1():
    #using count_zero only
    pass
solver()
#co cach 2(Trung)