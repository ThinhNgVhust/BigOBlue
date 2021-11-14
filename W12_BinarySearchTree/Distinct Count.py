t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    arr = len(set(input().strip().split()))
    if x < arr:
        print('Average')
    elif x > arr:
        print('Bad')
    else:
        print('Good')
