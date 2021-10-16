def _left(idx):
    return 2 * idx + 1


def _right(idx):
    return 2 * idx + 2


def _parent(idx):
    return (idx - 1) // 2


class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def __len__(self):
        return self.size

    def _max_heapify(self, idx):
        l = _left(idx)
        r = _right(idx)
        largest = idx
        if l < len(self) and self.arr[l] > self.arr[largest]:
            largest = l
        if r < len(self) and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != idx:
            self.arr[largest], self.arr[idx] = self.arr[idx], self.arr[largest]
            self._max_heapify(largest)

    def _build_max_heap(self):
        n = len(self)
        n = (n - 1) // 2
        for i in range(n, -1, -1):
            self._max_heapify(i)

    def sort(self):
        self._build_max_heap()
        while self.size:
            self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
            self.size -= 1
            self._max_heapify(0)
        self.size = len(self.arr)

    def insert(self, value):
        curr_idx = self.size
        self.arr.append(value)
        while (curr_idx - 1) // 2 >= 0 and self.arr[curr_idx] >= self.arr[(curr_idx - 1) // 2]:
            self.arr[curr_idx], self.arr[(curr_idx - 1) // 2] = self.arr[(curr_idx - 1) // 2], self.arr[curr_idx]
            curr_idx = (curr_idx - 1) // 2
        self.size += 1

    def extract(self):
        if self.size:  # need optimize
            self.size = len(self)
            self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
            self.size -= 1
            value = self.arr.pop()
            self._max_heapify(0)
            return value
        else:
            print("No more element in heap")


if __name__ == '__main__':
    heap = Heap([-1, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print("build heap")
    heap._build_max_heap()
    print(heap.arr)
    for i in range(len(heap)):
        print(heap.extract(),heap.arr)
# class PQEntry():
#     def __init__(self, value):
#         self.value = value
#
#     def __lt__(self, other):
#         return self.value > other.value
#
#     def __str__(self):
#         return str(self.value)
#
# arr = [-1, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# import heapq
# print(arr)
# arr1 = [PQEntry(x) for x in arr]
# heapq.heapify(arr1)
# print([x.value for x in arr1])