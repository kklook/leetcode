# 我这种写法不是比什么状态位简洁得多？
class Solution(object):
    
    def generateMatrix(self, n):
        if n == 0:
            return []
        dp = [[0] * n for i in range(n)]
        i, j = 0, 0
        tot = n * n
        num = 1
        dp[0][0] = 1
        while num < tot:
            while j < n - 1 and dp[i][j+1] == 0:
                j += 1
                num += 1
                dp[i][j] = num
            while i < n - 1 and dp[i+1][j] == 0:
                i += 1
                num += 1
                dp[i][j] = num
            while j > 0 and dp[i][j-1] == 0:
                j -= 1
                num += 1
                dp[i][j] = num
            while i > 0 and dp[i-1][j] == 0:
                i -= 1
                num += 1
                dp[i][j] = num
        return dp