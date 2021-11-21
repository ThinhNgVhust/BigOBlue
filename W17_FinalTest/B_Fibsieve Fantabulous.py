N = int(input())
arr = [int(x) for x in input().split()]
arr =[(arr[i],i+1) for i in range(len(arr))]

arr.sort()
ck = []
for i in range(1,N):
    if arr[i][0] ==arr[i-1][0]:
        ck.append([i,i-1])
        if ck==2:
            break

if len(ck)<2:
    print("NO")
    exit()
else:
    print("YES")
arr1 = [arr[i][1] for i in range(len(arr))]
print(" ".join([str(x) for x in arr1]))
arr[ck[0][1]],arr[ck[0][0]] = arr[ck[0][0]],arr[ck[0][1]]
arr1 = [arr[i][1] for i in range(len(arr))]
print(" ".join([str(x) for x in arr1]))
arr[ck[1][1]],arr[ck[1][0]] = arr[ck[1][0]],arr[ck[1][1]]
arr1 = [arr[i][1] for i in range(len(arr))]
print(" ".join([str(x) for x in arr1]))