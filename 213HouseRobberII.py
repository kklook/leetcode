

# 两边DP
class Solution(object):
    
    def rob(self, nums):
        bf, af = 0, 0
        if len(nums) > 1:
            for i in range(1, len(nums)):  # 不抢第一间
                if i % 2 == 0:
                    bf = max(bf + nums[i], af)
                else:
                    af = max(af + nums[i], bf)
            result = max(bf, af)
            bf, af = 0, 0
            for i in range(len(nums) - 1):  # 抢第一间
                if i % 2 == 0:
                    bf = max(bf + nums[i], af)
                else:
                    af = max(af + nums[i], bf)
            result = max(bf, af, result)
            return result
        else:
            return 0 if len(nums) == 0 else nums[0]