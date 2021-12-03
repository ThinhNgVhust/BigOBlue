class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def create_node(x):
    node = Node(x)
    return node


def insert_node(root, x):
    if root == None:
        return create_node(x)
    if x < root.key:
        root.left = insert_node(root.left, x)
    elif x > root.key:
        root.right = insert_node(root.right, x)
    return root


def create_bstree(arr):
    root = None
    for e in arr:
        root = insert_node(root, e)
    return root


def find_max(node):
    if node is None:
        return None
    pos = node.left
    node = node.left
    while node.right:
        pos = node.right
        node = node.right
    return pos.key


if __name__ == '__main__':
    # using hashtable + sort
    n = int(input())
    arr = [int(x) for x in input().split()]
    hash = {}
    for i in range(len(arr)):
        hash[arr[i]] = i
    arr.sort()
    minVal = 1e20
    for i in range(0, len(arr) - 1):
        if arr[i + 1] - arr[i] < minVal and hash[arr[i + 1]] < hash[arr[i]]:
            minVal = arr[i + 1] - arr[i]
    print(minVal)
