from collections import *

def solver():
    n, b = map(int, input().split(" "));
    arr = deque();
    count = 0;
    result = []
    for i in range(n):
        t, d = map(int, input().split(" "));
        while arr and arr[0] <= t:
            arr.popleft();
            count -= 1;
        if count <= b:
            if len(arr) > 0:
                t = max(arr[-1], t);
            y = d + t
            result.append(y)
            arr.append(y);
            count += 1;
        else:
            result.append(- 1)
    print(" ".join([str(x) for x in result]))
if __name__ == '__main__':
    solver()