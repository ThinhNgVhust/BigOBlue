
def eratosthenes(n):
    # return list of prime number less than or equal N
    # NloglogN
    mark = [True] * (n + 1)
    mark[0] = False
    # mark[1] = False
    i = 2
    while i * i <= n:
        if mark[i] is True:
            for j in range(int(i * i), n + 1, i):
                mark[j] = False
        i += 1
    ans = []
    for i in range(len(mark)):
        if mark[i]: ans.append(i)
    return ans

def solver():
    while True:
        try:
            n,c = map(int,input().split())
            arr = eratosthenes(n)
            mid = len(arr)//2
            ans = []
            if len(arr)%2 ==0:
                print("{0} {1}: ".format(n, c), end="")
                #vuot qua danh sach
                if 2*c > len(arr):
                    print(" ".join([str(x) for x in arr]))
                else:
                    for i in range(mid-c,mid+c):
                        ans.append(arr[i])
                    print(" ".join([str(x) for x in ans]))

            elif len(arr)%2 !=0:
                print("{0} {1}: ".format(n, c), end="")
                if 2*c-1 > len(arr):
                    print(" ".join([str(x) for x in arr]))
                else:
                    for i in range(mid-c+1,mid+c):
                        ans.append(arr[i])
                    print(" ".join([str(x) for x in ans]))
            print()
        except EOFError:
            return
solver()