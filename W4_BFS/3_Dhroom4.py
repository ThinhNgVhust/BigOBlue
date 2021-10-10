'''
Link:
Time complexity:
Space complexity:
'''
from collections import deque, defaultdict

MODULE =int(1e5)
def BFS(k, l, a):
    q = deque()
    visited = defaultdict()
    visited[k] = 0
    q.append(k)
    while q:
        k = q.popleft()
        for i in a:
            x = (k * i) % MODULE
            if x not in visited:
                visited[x] = visited[k] + 1
                if x == l:
                    return visited[x]
                q.append(x)
    return -1


if __name__ == '__main__':
    k, l = list(map(int, input().split()))
    N = int(input())
    a = list(map(int, input().split()))
    if k == l:
        print(0)
    else:
        print(BFS(k, l, a))