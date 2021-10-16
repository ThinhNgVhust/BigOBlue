import heapq
while True:
    N = int(input())
    if N == 0:
        break

    arr = [int(x) for x in input().split()]
    # print(arr)
    # heapq.heapify(arr)
    # print("heap",arr)
    cost = 0
    while len(arr)>1:
        value1 = heapq.heappop(arr)
        value2 = heapq.heappop(arr)
        s= value1+value2
        cost+=s
        heapq.heappush(arr,s)
    print(cost)

