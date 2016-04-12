

class Solution(object):
    
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        dp = [0 for i in range(num+1)]
        for i in range(1,num+1):
            if i % 2 == 0:
                dp[i] = dp[i / 2]
            else:
                dp[i] = dp[i / 2] + 1
        return dp