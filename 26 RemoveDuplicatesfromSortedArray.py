

class Solution(object):
    
    def removeDuplicates(self, nums):
        l = len(nums)
        i = 0
        t = 0
        while i < l:
            t = nums.pop(0)
            if len(nums) == 0 or t != nums[-1]:
                nums.append(t)
            i += 1
        return len(nums)