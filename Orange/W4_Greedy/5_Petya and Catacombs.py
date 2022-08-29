def solver1():
    n = int(input())
    arr =[0]
    arr.extend([int(x) for x in input().split()])
    room = [-1 for i in range(n+1)]
    room[0]=1
    cnt = 1
    for i in range(1,n+1):
        if room[arr[i]]!=-1:
            room[i]=room[arr[i]]
            room[arr[i]]=-1
        else:
            cnt+=1
            room[i]=cnt
    print(cnt)

def solver2():
    n = int(input())
    arr = [int(x) for x in input().split()]
    cnt = 0
    arr.sort()
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            cnt+=1
    print(cnt+1)

# solver()