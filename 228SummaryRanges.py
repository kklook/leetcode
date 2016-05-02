

# 模拟
class Solution(object):
    
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return str(nums[0]),
        bf = nums[0]
        result = [str(bf)]
        for i in range(1, len(nums)):
            if nums[i] == bf + 1 and i == len(nums) - 1:
                result[-1] += '->' + str(nums[i])
            if nums[i] != bf + 1:
                if not result[-1] == str(bf):
                    result[-1] += '->' + str(bf)
                result += str(nums[i]),
            bf = nums[i]
        return result