class Node:
    def __init__(self, val=0):
        self.value = val
        self.next = None
        self.pre = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def apppend(self, key):
        node = Node(key)
        pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        node.pre = pre
        pre.next = node

    def erase(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre

        # node is auto delete by garbarge collection

    def end(self):
        return self.tail

    def begin(self):
        return self.head.next

    def print_list(self):
        tmp = self.head.next
        print("Start->", end=" ")
        while tmp and tmp != self.tail:
            print(tmp.value, "->", end=" ")
            tmp = tmp.next
        print("End")


class RLUCache:
    def __init__(self, cap):
        self.capaciy = cap
        self.dll = DoubleLinkedList()
        self.cache = {}  # key: (value, Node(key))

    def get(self, key):
        """
        lấy 1 giá trị của 1 khóa đã tồn tại trong cache.
        :return:Trả về giá trị nếu tồn tại, nếu không trả về null
        """
        if key in self.cache:
            self.dll.erase(self.cache[key][1])
            self.dll.apppend(key)
            self.cache[key][1] = self.dll.end().pre
            return self.cache[key][0]
        return "NULL"

    def set(self, key, value):

        """
        Bỏ 1 cặp (key,value) vào trong cache, nếu cache đầy thì loại bỏ bớt cặp cũ nhất để chèn cặp mới vào
        :param key:
        :param value:
        :return:
        """

        if len(self.cache) == self.capaciy and key not in self.cache:
            self.cache.pop(self.dll.begin().value)
            self.dll.erase(self.dll.begin())
        elif key in self.cache:
            self.dll.erase(self.cache[key][1])
        self.dll.apppend(key)
        self.cache[key] = [value, self.dll.end().pre]


if __name__ == '__main__':
    cache = RLUCache(cap=3)
    cache.set(1, "John")
    cache.set(2, "Usha")
    cache.set(3, "Summer")
    cache.set(4, "Summer")
    print(cache.get(2))
    print(cache.get(1))
    cache.set(5, "Alice")
    print(cache.get(3))
    print(cache.get(2))

    cache.set(1, "John")
    cache.set(1, "John")
