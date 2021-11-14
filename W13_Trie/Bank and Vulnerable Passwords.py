class TrieNode:
    def __init__(self, char):
        self.countWord = 0
        self.children = {}
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode("X")
        self.max = 0
        self.flag  = True
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if node.countWord > 0:
               return False
        node.countWord+=1
        if node.countWord>1:
            return False
        if len(node.children.keys())>0:
            return False
        return True

trie = Trie()
N = int(input())
check = False
for i in range(1,N+1):
    flag = trie.insert(input())
    if flag is False:
        print("vulnerable")
        check = True
        break
if check is False:
    print("non vulnerable")