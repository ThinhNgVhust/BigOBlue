class Node:
    def __init__(self):
        self.child = [None, None]
        self.parent = None
        self.isBlock = False


def insert(root, e):
    if root.isBlock: return ""
    tmp = root
    result = ""
    for i in range(e):
        l = tmp.child[0]
        r = tmp.child[1]
        next = -1
        if l is None or l.isBlock is False:
            next = 0
        elif r is None or r.isBlock is False:
            next = 1
        if next == -1:
            return ""
        if tmp.child[next] is None:
            tmp.child[next] = Node()
            tmp.child[next].parent = tmp
        tmp = tmp.child[next]
        result += str(next)
    tmp.isBlock = True
    while tmp.parent:
        tmp = tmp.parent
        l = tmp.child[0]
        r = tmp.child[1]
        if l is not None and r is not None and l.isBlock is True and r.isBlock is True:
            tmp.isBlock = True
    return result


def solver():
    N = int(input())
    arr = [int(x) for x in input().split()]
    arr = [(arr[i], i) for i in range(len(arr))]
    arr.sort()
    root = Node()
    ans = [0] * len(arr)
    for e, idx in arr:
        s = insert(root, e)
        if len(s) > 0:
            ans[idx] = s
        else:
            print("NO")
            return
    print("YES")
    for s in ans:
        print(s)


solver()
