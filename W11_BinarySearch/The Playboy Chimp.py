import bisect

n = int(input())

arr = [int(x) for x in input().split()]
q = int(input())
Q = [int(x) for x in input().split()]
for e in Q:
    insertion_left = bisect.bisect_left(arr, e, 0)
    insertion_right = bisect.bisect_right(arr, e, 0)
    str1 = ""
    if insertion_left==0:str1="X"
    else:str1 = str(arr[insertion_left-1])
    str2 = ""
    if insertion_right==n:str2="X"
    else:str2=str(arr[insertion_right])
    result = str1+" "+str2
    print(result)

