arr = [10, 13, 51, 64, 5, 21, 32]


def merge(A, B, arr):
    pt1 = 0
    pt2 = 0
    i = 0
    while pt1 < len(A) and pt2 < len(B):
        if A[pt1] < B[pt2]:
            arr[i] = A[pt1]
            pt1 += 1
            i += 1
        else:
            arr[i] = B[pt2]
            pt2 += 1
            i += 1

    while pt1 < len(A):
        arr[i] = A[pt1]
        pt1 += 1
        i += 1
    while pt2 < len(B):
        arr[i] = B[pt2]
        pt2 += 1
        i += 1


def merge_sort(arr):
    if len(arr) > 1:
        n = len(arr)
        hafl = n // 2
        A = [arr[i] for i in range(hafl)]
        B = [arr[i] for i in range(hafl, n)]
        merge_sort(A)#devide and conquer
        merge_sort(B)#devide and conquer
        merge(A, B, arr)#Combine


print("arr: ", arr)
merge_sort(arr)
print("arr: ", arr)
