ans = 0
import sys
sys.setrecursionlimit(2000)

def solver():
    trie = {}
    s = input()
    good_str = input()
    k = int(input())
    is_good = {}
    for i in range(26):
        if good_str[i] == "0":
            is_good[chr(ord("a") + i)] = False
        else:
            is_good[chr(ord("a") + i)] = True
    for i in range(len(s)):
        root = trie
        for j in range(i, len(s)):
            if s[j] not in root:
                root[s[j]] = {}
            root = root[s[j]]
    dfs(trie, is_good, 0, k)
    global ans
    print(ans - 1)


def dfs(node, is_good, level, limitation):
    if level <= limitation:
        global ans
        ans += 1
    for key in node:
        if key != 1:
            if is_good[key] is False:
                dfs(node[key], is_good, level + 1, limitation)
            else:
                dfs(node[key], is_good, level, limitation)


solver()
