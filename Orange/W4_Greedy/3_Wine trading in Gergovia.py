def solver():
    while True:
        n = int(input())
        if n == 0:
            return
        arr = [int(x) for x in input().split()]
        buy = []
        sell = []
        for i in range(len(arr)):
            if arr[i] >= 0:
                buy.append(i)
            else:
                arr[i] = arr[i] * -1
                sell.append(i)
        pt_s = 0
        pt_b = 0
        ans = 0
        while pt_s<len(sell) and pt_b<len(buy):
            if arr[sell[pt_s]] < arr[buy[pt_b]]:
                ans += abs(sell[pt_s] - buy[pt_b]) * ( arr[sell[pt_s]])
                arr[buy[pt_b]] -= arr[sell[pt_s]]
                arr[sell[pt_s]] = 0
                pt_s += 1
            elif arr[sell[pt_s]] > arr[buy[pt_b]]:
                ans += abs(sell[pt_s] - buy[pt_b]) * (arr[buy[pt_b]])
                arr[sell[pt_s]] -= arr[buy[pt_b]]
                arr[buy[pt_b]] = 0
                pt_b += 1
            else:
                ans += abs(sell[pt_s] - buy[pt_b]) * (arr[sell[pt_s]])
                arr[buy[pt_b]] = 0
                arr[sell[pt_s]] = 0
                pt_s += 1
                pt_b += 1
        print(ans)

solver()
