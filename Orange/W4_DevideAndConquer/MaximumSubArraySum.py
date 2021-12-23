arr = [-3, -8, 7, -2, -3, 5, -4, 6, -9, 2]
MIN = -int(1e20)


def bruteforce(arr):
    n = len(arr)
    maxSum = arr[0]
    for i in range(n):
        for j in range(i + 1, n):
            sub_arr = arr[i:j]
            maxSum = max(maxSum, sum(sub_arr))
    print(maxSum)  # (N^2)


bruteforce(arr)


def combine_sol(arr, left, mid, right):
    max_part_left = MIN
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += arr[i]
        if sum >= max_part_left:
            max_part_left = sum
    max_part_right = MIN
    sum = 0
    for i in range(mid + 1, right):
        sum += arr[i]
        if sum >= max_part_right:
            max_part_right = sum
    return (max_part_left + max_part_right)


def devide_and_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left_sum = devide_and_conquer(arr, left, mid)
    max_right_sum = devide_and_conquer(arr, mid + 1, right)
    max_mid_sum = combine_sol(arr, left, mid, right)
    return max(max_left_sum, max_mid_sum, max_right_sum)

def kadane_DP(arr):
    pass
print("arr ", arr)
print("Devide and conquer ", devide_and_conquer(arr, 0, len(arr)))
