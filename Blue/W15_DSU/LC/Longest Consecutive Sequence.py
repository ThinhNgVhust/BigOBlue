class Solution:
    def __init__(self):
        self.ranks = None
        self.parent = None

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        up = self.find(u)
        vp = self.find(v)
        if up == vp:
            return
        if up > vp:
            self.parent[vp] = up
        elif vp > up:
            self.parent[up] = vp
        else:
            self.parent[up] = vp
            self.ranks[vp] += 1
        return

    def longestConsecutive(self, nums):
        # -> int
        nums = set(nums)
        n = len(nums)
        Adj = {}
        # O(n)
        self.ranks = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
        for idx, num in enumerate(nums):
            Adj[num] = idx
        for key in Adj:
            if key - 1 in Adj:
                self.union(Adj[key], Adj[key - 1])
            if key+1 in Adj:
                self.union(Adj[key], Adj[key + 1])
        Adj={}
        for i in range(n):
            self.find(i)
            if self.parent[i] not in Adj:
                Adj[self.parent[i]] = 0
            Adj[self.parent[i]] +=1
        result = 0
        for k in Adj:
            result =max(result,Adj[k])
        print(result)
        return result
nums = [100,4,200,1,3,2]
Solution().longestConsecutive(nums)