# DP
class Solution(object):
    
    def numDistinct(self, s, t):
        dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(s)][len(t)]