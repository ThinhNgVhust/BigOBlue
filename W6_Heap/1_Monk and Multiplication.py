# '''
# Topic:
# Source:
# Time Comlexity:O()
# Space Comlexity:O()
# '''

class PQEntry():
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)


import heapq

N = int(input())

arr = list(map(int, input().split()))

heap = []

for i in arr:

    heapq.heappush(heap, -i)

    if len(heap) < 3:
        print(-1)

        continue

    top1 = heapq.heappop(heap)

    top2 = heapq.heappop(heap)

    top3 = heapq.heappop(heap)

    print(-1 * top1 * top2 * top3)

    heapq.heappush(heap, top1)

    heapq.heappush(heap, top2)

    heapq.heappush(heap, top3)
