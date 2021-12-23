def solver():
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        b = int(input(), 2)
        arr.append(b)
    min_dis = 30
    for i in range(n):
        for j in range(i + 1, n):
            a = arr[i]
            b = arr[j]
            min_dis = min(min_dis, bin(a ^ b).count("1"))
    print(min_dis)


solver()
