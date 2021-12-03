"""
Topic:
Source:
Time Comlexity:O()
Space Comlexity:O()
"""

import heapq


def solver():
    m = []
    N = int(input())
    di = {}
    for i in range(N):
        b = input().split()
        if b[0] == '1':
            b = int(b[1])
            if b not in di or di[b] ==2:
                heapq.heappush(m, b)
                di[b] = 1
        elif b[0] == '2':
            b = int(b[1])
            di[b]=2
        else:
            while di[m[0]] == 2:
                heapq.heappop(m)
                # del di[m[0]]
            print(m[0])


if __name__ == '__main__':
    solver()
