class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.ans = []
        self.tmp = []
        self.visited = [False] * n
        self.k = 0
        self.solve(n, k)
        ans = ""
        for e in self.ans[-1]:
            ans += str(e + 1)
        return ans

    def solve(self, n, k):
        if len(self.tmp) == n:
            self.k += 1
            if self.k == k:
                self.ans.append(self.tmp.copy())
        else:
            if self.k == k: return
            for i in range(n):
                if self.visited[i] is False:
                    self.visited[i] = True
                    self.tmp.append(i)
                    self.solve(n, k)
                    self.visited[i] = False
                    self.tmp.pop()
sol =Solution()
print(sol.getPermutation(9,217778))