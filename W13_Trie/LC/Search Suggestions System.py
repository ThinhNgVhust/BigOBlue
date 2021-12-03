class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


def char2idx(char):
    return ord(char) - ord("a")


def idx2char(idx):
    return chr(ord("a") + idx)


def insert(node, word):
    tmp = node
    for char in word:
        idx = char2idx(char)
        if tmp.children[idx] is None:
            tmp.children[idx] = Node()
        tmp = tmp.children[idx]
    tmp.count += 1
    pass


def dfs(node, word, result):
    if len(result) >= 3: return
    if node.count > 0:
        result.append(word)
    for i in range(len(node.children)):
        if node.children[i] is not None:
            dfs(node.children[i], word + idx2char(i), result)


def find(word, node, result):
    tmp = node
    for char in word:
        idx = char2idx(char)
        if tmp.children[idx] is not None:
            tmp = tmp.children[idx]
        else:
            return []
    dfs(tmp, word, result)


class Solution:
    def __init__(self):
        self.root = Node()

    def suggestedProducts(self, products, searchWord):
        # -> List[List[str]]:
        for word in products:
            insert(self.root, word)
        result = []
        for i in range(len(searchWord)):
            tmp = []
            find(searchWord[:i + 1], self.root, tmp)
            result.append(tmp)
        return result


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
sol = Solution()
sol.suggestedProducts(products,searchWord)