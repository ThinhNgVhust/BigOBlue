n,s =map(int,input().split())
arr = []
import math
for i in range(n):
    x,y,i = map(int,input().split())
    dist = math.sqrt(x**2 + y**2)
    arr.append((dist,i))
arr.sort()
ans = False
for e in arr:
    dist,i = e[0],e[1]
    s+=i
    if s>=int(1e6):
        print("{:.7f}".format(dist))
        # print(dist)
        ans = True
        break
if ans is False:print("-1")