

# dp边界搞得头疼
class Solution(object):
    
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if not all((s1,s2,s3)):
            return s1 + s2 == s3
        s1, s2, s3 = list(s1), list(s2), list(s3)
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if j > 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[len(s1)][len(s2)]