import sys
coins = [i * i * i for i in range(1, 22)]

MAX = 10000
total = [0]*(MAX+1)
total[0] = 1
for coin in coins:
    for i in range(coin,MAX+1):
        total[i] = total[i]+total[i-coin]
arr = sys.stdin.read().split()
arr =[int(x) for x in arr]
for e in arr:
    print(total[e])