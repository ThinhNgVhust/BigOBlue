class PQEntry():
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)


import heapq as h


def solver():
    N = int(input())
    max_heap = []
    min_heap = []
    n_elements = 0
    for i in range(N):
        s = input()
        if len(s) > 1:
            a, b = map(int, s.split())
            b1 = PQEntry(b)
            n_elements += 1
            if n_elements < 3:
                h.heappush(max_heap, b1)
            elif n_elements % 3 != 0:
                if len(min_heap) == 0:
                    element = h.heappop(max_heap)
                    h.heappush(min_heap, element.value)
                elif b1.value > min_heap[0]:
                    value = h.heappop(min_heap)
                    h.heappush(min_heap, b1.value)
                    value1 = PQEntry(value)
                    h.heappush(max_heap, value1)
                else:
                    h.heappush(max_heap, b1)
            elif n_elements % 3 == 0:
                h.heappush(max_heap, b1)
                obj = h.heappop(max_heap)
                h.heappush(min_heap, obj.value)

        else:
            if len(min_heap) == 0:
                print("No reviews yet")
            else:
                print(min_heap[0])


if __name__ == '__main__':
    solver()
