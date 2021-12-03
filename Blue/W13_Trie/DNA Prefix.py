class TrieNode:
    def __init__(self, char):
        self.countWord = 0
        self.children = {}
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode("root")
        self.max = 0
    def insert(self, word):
        node = self.root
        i = 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
                node.children[char].countWord=1
            else:
                node.children[char].countWord += 1
            # self.max = max(self.max,node.children[char].countWord)
            node = node.children[char]
            i+=1
        # node.countWord += 1
        return node

    def traverse(self):
        node = self.root
        frontier = [node]
        level = 1
        while frontier:
            next = []
            for node in frontier:
                for sub in node.children.keys():
                    child = node.children[sub]
                    next.append(child)
                    self.max = max(self.max,child.countWord*level)
            level+=1
            frontier=next
        return  self.max

if __name__ == '__main__':
    T = int(input())

    for case in range(1, T + 1):
        trie = Trie()
        N = int(input())
        for i in range(N):
            code = input()
            trie.insert(code)
        trie.traverse()
        print("Case {0}: {1}".format(case,trie.max))

