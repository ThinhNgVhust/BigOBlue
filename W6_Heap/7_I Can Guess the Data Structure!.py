import heapq


class PQEntry():
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)


from collections import deque


def solve():
    while True:
        N = int(input())
        q = deque()
        s = []
        priority_queue = []
        is_q = True
        is_s = True
        is_priority = True
        for _ in range(N):
            a, b = map(int, input().split())
            if a == 1:
                if is_s:
                    s.append(b)
                if is_q:
                    q.append(b)
                if is_priority:
                    heapq.heappush(priority_queue, PQEntry(b))
            else:
                if is_s:
                    if len(s) == 0 or s[-1] != b:
                        is_s = False
                    else:
                        s.pop()
                if is_q:
                    if len(q) == 0 or q[0] != b:
                        is_q = False
                    else:
                        q.popleft()
                if is_priority:
                    if len(priority_queue) == 0 or priority_queue[0].value != b:
                        is_priority = False
                    else:
                        heapq.heappop(priority_queue)
        if is_q and is_s is False and is_priority is False:
            print("queue")
        elif is_s and is_q is False and is_priority is False:
            print("stack")
        elif is_priority and is_q is False and is_s is False:
            print("priority queue")
        elif not is_s and not is_q and not is_priority:
            print("impossible")
        else:
            print("not sure")


def solver():
    try:
        solve()
    except:
        return


if __name__ == '__main__':
    solver()
