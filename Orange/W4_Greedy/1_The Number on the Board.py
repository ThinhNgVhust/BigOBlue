def method_heap():
    import heapq
    k = int(input())
    n = int(input())
    arr = []
    while n != 0:
        arr.append(n % 10)
        n = n // 10
    # print(arr)
    arr.reverse()
    # print(arr)
    s = sum(arr)
    if s > k:
        print("0")
        # exit()
    else:
        ans = 0
        heapq.heapify(arr)
        k = k - s
        while k > 0:
            if len(arr) > 0:
                element = heapq.heappop(arr)
            else:
                print("0")
                exit()
            k -= 9 - element
            ans += 1
        print(ans)
    # 70
    # 3326631213
def method2():
    k = int(input())
    n =input()
    arr =[0 for i in range(10)]
    for char in n:
        number = int(char)
        arr[number]+=1
    ans = 0
    s = 0
    for i in range(len(arr)):
        s+=i*arr[i]
    if s>=k:
        print("0")
    else:
        k-=s
        s=0
        for i in range(len(arr)-1):
            cnt = arr[i]
            for j in range(cnt):
                s=s+(9-i)
                ans+=1
                if s>=k:
                    print(ans)
                    return
        print(ans)
method2()