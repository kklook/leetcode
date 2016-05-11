# 模拟
class Solution(object):
    
    def multiply(self, num1, num2):
        dp = [0 for i in range(len(num1) + len(num2))]
        n = 0
        for i in range(len(num1) - 1, -1, -1):
            m = 0
            for j in range(len(num2) - 1, -1, -1):
                dp[n+m] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                m += 1
            n += 1
        t = 0
        print dp
        for i in range(len(dp)):
            dp[i] += t
            t = dp[i] / 10
            dp[i] = str(dp[i] % 10)
        while len(dp) > 1 and dp[-1] == '0':
            dp.pop()
        dp.reverse()
        return "".join(dp)