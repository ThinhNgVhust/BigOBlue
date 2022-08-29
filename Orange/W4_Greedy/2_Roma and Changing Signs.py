import heapq


def solver():
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    for i in range(len(arr)):
        if k > 0 and arr[i] < 0:
            arr[i] = -arr[i]
            k -= 1
    arr.sort()
    if k % 2 == 1:
        arr[0] = -arr[0]
    print(sum(arr))


if __name__ == '__main__':
    solver()
