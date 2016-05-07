

# 排字典序就可以了
class Solution:

    def largestNumber(self, nums):
        nums = sorted([str(s) for s in nums], cmp = self.cmp)
        result = "".join(nums).lstrip('0')
        return result or '0'
    
    def cmp(self, a, b):
        return [1, -1][a + b > b + a]