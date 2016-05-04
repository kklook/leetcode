

# 筛表
class Solution(object):
    
    def countPrimes(self, n):
        if n < 3:
            return 0
        dp = [False for i in range(n)]
        for i in range(3, n):
            if i % 2 == 1:
                dp[i] = True
        for i in range(3, int(math.sqrt(n)) + 1):
            if dp[i]:
                for j in range(i + i, n, i):
                    dp[j] = False
        count = 1
        for i in range(n):
            if dp[i]:
                count += 1
        return count