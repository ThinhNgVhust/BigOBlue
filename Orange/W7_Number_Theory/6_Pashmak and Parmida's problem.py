def solver():
    n = int(input())
    arr = [int(x) for x in input().split()]
    fre = {}
    for i in range(len(arr)):
        if arr[i] not in fre:
            fre[arr[i]] = []
        fre[arr[i]].append(i)
    pre = [0] * n
    suf = [0] * n
    for key in fre:
        i = 1
        for e in fre[key]:
            pre[e] = i
            suf[e] = len(fre[key]) - i + 1
            i += 1
    ans = solve(pre, suf)
    print(ans)


def solve(A, B):
    if len(A) <= 1: return 0
    mid = len(A) // 2
    ans = 0
    A1 = A[:mid]
    A2 = A[mid:]
    B1 = B[:mid]
    B2 = B[mid:]
    if len(A1) >= 1 and len(B1) >= 1:
        ans = solve(A1, B1) + solve(A2, B2)
    else:
        A.sort()
        B.sort()
    len_A = len(A1)
    index_A = 0
    len_B = len(B2)
    index_B = 0

    for k in range(len_A + len_B):

        if A1[index_A] <= B2[index_B]:

            index_A += 1
            if index_A == len_A:
                merge(A1, A2, A)
                merge(B1, B2, B)

                return ans
        else:
            index_B += 1
            ans += (len_A - index_A)

            if index_B == len_B:
                merge(A1, A2, A)
                merge(B1, B2, B)
                return ans


def merge(A1, A2, dest):
    i = 0
    j = 0
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            dest[i + j] = A1[i]
            i += 1
        else:
            dest[i + j] = A2[j]
            j += 1
    while i < len(A1):
        dest[i + j] = A1[i]
        i += 1

    while j < len(A2):
        dest[i + j] = A2[j]
        j += 1


solver()
