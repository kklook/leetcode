

# DP
class Solution(object):
    
    def rob(self, nums):
        bf = 0
        af = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                bf = max(bf + nums[i], af)
            else:
                af = max(af + nums[i], bf)
        return max(bf, af)