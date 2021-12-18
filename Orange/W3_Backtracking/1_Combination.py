result = []


def solver():
    # k = 6
    while True:
        arr = input().split()
        if len(arr) == 1:
            return
        arr = arr[1:]
        combination(arr, result, 6, 0)
        print()


def combination(arr, result, k, left):
    if len(result) == k:
        print(" ".join(result))
        return
    for i in range(left, len(arr)):
        result.append(arr[i])
        combination(arr, result, k, i + 1)
        result.pop()


solver()
