# dp + dfs 不知道是不是最优
class Solution(object):
    
    def partition(self, s):
        dp = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = True
                        dp[j][i] = True
                    if i < len(s) - 1 and j > 1 and dp[i+1][j-1] == True:
                        dp[i][j] = True
                        dp[j][i] = True
                    if j < len(s) - 1 and i > 1 and dp[j+1][i-1] == True:
                        dp[i][j] = True
                        dp[j][i] = True
        resultList = []
        print dp
        def dfs(i, result):
            if i == len(s):
                resultList.append(result)
            for j in range(i, len(s)):
                if dp[i][j] == True:
                    dfs(j + 1, result + [s[i:j+1]])
        dfs(0, [])
        return resultList