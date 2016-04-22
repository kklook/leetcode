

#可能原意不是这个吧...
class Solution(object):
    
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        d = {}
        maxnum = 1
        for i in nums:
            if not i in d:
                d[i] = 1
                maxnum = max(i, maxnum)
        i = 1
        while True:
            if not i in d:
                return i
            i += 1