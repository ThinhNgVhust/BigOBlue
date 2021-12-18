ans = []
min_val = int(1e20)
def solver():
    global ans
    arr = [int(x) for x in input().split()]
    n = len(arr)
    result = []
    visited =[False]*n
    permutation(arr, 4, result,visited)
    print(" ".join([str(x) for x in ans]))
    pass
def permutation(arr,k,result,visited):
    global  min_val,ans
    if len(result)==k:
        a = arr[result[0]]
        b = arr[result[1]]
        c = arr[result[2]]
        d = arr[result[3]]
        q = round(abs((a*d -c*b)/(d*b)),20)
        if q < min_val:
            ans = result.copy()
            min_val = q
        return
    for i in range(len(arr)):
        if visited[i] :continue
        visited[i]=True
        result.append(i)
        permutation(arr,k,result,visited)
        visited[i]=False
        result.pop()
solver()