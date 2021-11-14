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
    def insert(self, word,time):
        flag = True
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if node.countWord > 0:
                flag = False
        node.countWord += time
        if flag is False:
            return flag,word
        else:
            if len(node.children.keys()) > 0:
                return False,word
        #         result = word
        #         frontier =[node.children[list(node.children.keys())[0]]]
        #         while frontier:
        #             next = []
        #             for node in frontier:
        #                 for sub in node.children.keys():
        #                     result+=sub
        #                     next.append(node.children[sub])
        #                     break
        #                 break
        #             frontier = next
        #         return False,result
        return True,None

trie = Trie()
N = int(input())
check = False
for i in range(1,N+1):
    flag,word = trie.insert(input(),i)
    if flag is False:
        print("BAD SET")
        print(word)
        check = True
        break
if check is False:
    print("GOOD SET")