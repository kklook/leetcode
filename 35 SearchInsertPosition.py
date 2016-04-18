

class Solution(object):
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if i > 0 and target < nums[i] and target > nums[i-1]:
                return i
        