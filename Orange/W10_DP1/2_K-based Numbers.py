def solver():
    n = int(input())
    k = int(input())
    char = "1"
    ans = solve(0,n,k,char)
    print(ans)


def solve(index,lenth,base_k,char):
    if index == 0:
        return (base_k-1)*solve(index+1,lenth,base_k,char)
    if index ==lenth:return 1
    if char !="0":
        return (base_k-1)*solve(index+1,lenth,base_k,char) + solve(index+1,lenth,base_k,"0")
    else:
        return (base_k-1)*solve(index+1,lenth,base_k,"1")

solver()