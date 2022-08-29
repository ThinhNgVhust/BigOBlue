dp = [[-1 for i in range(100)]for j in  range(100)]
def LCS(s1,s2,m,n):
    #m is length of s1
    #n is length of s2
    for i in range(0,len(s1)+1):
        for j in range(0,len(s2)+1):
            if i == 0 or j == 0:
                dp[i][j] =0
            elif s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
s1 = "BADCJEFGYT"
s2 = "ATCJDZEFGY"
print(LCS(s1,s2,len(s1),len(s2)))