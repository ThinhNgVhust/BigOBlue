MAX = int(1e10)
MIN = 1


def solver():
    while True:
        try:
            n, k = map(int, input().split())
            arr = [int(x) for x in input().split()]
            solve_one(arr, k)
        except EOFError:
            return


def Try(arr, C, k):
    # fill all e in arr with k box, each box has capacity C
    capacity = C
    cnt = 1
    for e in arr:
        if e > C:  # sua o thung chua nho hon sua o bang chuyen
            return False
        if e > capacity:
            if cnt == k:
                return False
            capacity = C
            cnt += 1
        capacity -= e
    return True


def solve_one(arr, k):
    L = MIN
    R = MAX
    ans = R
    for i in range(100):
        mid_capacity = (L + R) // 2
        if Try(arr, mid_capacity, k):
            ans = min(ans, mid_capacity)
            R = mid_capacity
        else:
            L = mid_capacity
    print(ans)


solver()
