import sys

sys.setrecursionlimit(100000)


def dq(arr):
    val = 0
    if len(arr) == 1:
        # if arr[left]==0:return 0
        return 1
    val = min(arr)
    # print("val",val)
    arr = [x - val for x in arr]

    tmp = []
    # print(arr)
    for i in range(len(arr)):
        if arr[i] != 0:
            tmp.append(arr[i])
        else:
            if len(tmp) > 0:
                # print(tmp)
                val += dq(tmp)
                tmp = []
    if len(tmp) > 1:
        val += dq(tmp)
        tmp = []
    # print("result ",val,arr)
    return min(val, len(arr))


def solver():
    n = int(input())
    arr = [int(x) for x in input().split()]
    # arr =[x for x in range(1,5001)]
    ans = dq(arr)
    print(ans)


solver()	