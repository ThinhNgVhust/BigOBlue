dp = [[-1 for i in range(100)]for j in  range(100)]
def LCS(s1,s2,m,n):
    if m == 0 or n == 0:
        dp[m][n] =0
        return dp[n][m]
    if dp[n][m]!=-1:
        return dp[n][m]
    if s1[m-1] == s2[n-1]:
        dp[n][m]=1+LCS(s1,s2,m-1,n-1)
        return dp[n][m]
    else:
        dp[n][m] = max(LCS(s1,s2,m-1,n),LCS(s1,s2,m,n-1))
        return dp[n][m]

s1 = "BADCJEFGYT"
s2 = "ATCJDZEFGY"
print(LCS(s1,s2,len(s1),len(s2)))