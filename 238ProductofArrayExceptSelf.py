# 6的飞起
class Solution(object):
    
    def productExceptSelf(self, nums):
        dp = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            dp[i+1] = product
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            dp[i-1] *= product
        return dp