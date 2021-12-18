# Task, show all subset of list
arr = [3, 4, 5, 1, 7]


def search_1(arr):
    n = len(arr)
    k = 1 << n
    for i in range(k):
        subset = []
        for b in range(n):
            if i & 1 << b != 0: subset.append(arr[b])
        print(subset)


def search_2(arr, subset, k):
    if k == len(arr):
        print(subset)
    else:
        search_2(arr, subset, k + 1)
        subset.append(arr[k])
        search_2(arr, subset, k + 1)
        subset.pop()


subset = []
search_2(arr, subset, 0)
