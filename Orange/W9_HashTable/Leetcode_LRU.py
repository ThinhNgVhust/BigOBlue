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


class LRUCache:

    def __init__(self, capacity: int):
        self.capaciy = capacity
        self.dll = DoubleLinkedList()
        self.cache = {}  # key: (value, Node(key))

    def get(self, key: int) -> int:
        if key in self.cache:
            self.dll.erase(self.cache[key][1])
            self.dll.apppend(key)
            self.cache[key][1] = self.dll.end().pre
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capaciy and key not in self.cache:
            self.cache.pop(self.dll.begin().value)
            self.dll.erase(self.dll.begin())
        elif key in self.cache:
            self.dll.erase(self.cache[key][1])
        self.dll.apppend(key)
        self.cache[key] = [value, self.dll.end().pre]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)