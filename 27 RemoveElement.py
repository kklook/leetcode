

class Solution(object):
    
    def removeElement(self, nums, val):
        i = 0
        t = 0
        l = len(nums)
        while i < l:
            t = nums.pop(0)
            if t != val:
                nums.append(t)
            i += 1
        return len(nums)