class Solution:
    def countPrimes(self, n: int):
        if n == 0 or n ==1:return 0
        check = [True for i in range(n)]
        check[0] = False
        check[1] = False
        i = 2
        while i * i <= n:
            if check[i] == True:
                for j in range(i + i, n, i):
                    check[j] = False
            i += 1
        cnt = 0
        for i in range(len(check)):
            if check[i] is True:
                # print(i)
                cnt += 1
        return cnt


sol = Solution()
print(sol.countPrimes(25))
