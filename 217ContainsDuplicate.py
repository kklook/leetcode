

class Solution(object):
    
    def containsDuplicate(self, nums):
        nums.sort()
        p = list(set(nums))
        p.sort()
        return not nums == p
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        