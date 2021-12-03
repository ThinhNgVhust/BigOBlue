from bisect import bisect_left, bisect_right
arr = [1,2,2,2,3,4,5,6,6,7]
print(bisect_left(arr,5,0))
print(bisect_right(arr,5,0))