# DP
class Solution(object):
    
    def minDistance(self, word1, word2):
        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)
        dp = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        # 因为零行被占用, 所以要后移一位保证运算次数
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                temp = 0
                # dp[i-1][j-1] 交换
                # dp[i-1][j], dp[i][j-1] 添加删除
                if word1[i-1] == word2[j-1]:
                    temp = dp[i-1][j-1]
                else:
                    temp = dp[i-1][j-1] + 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, temp)
        return dp[len(word1)][len(word2)]