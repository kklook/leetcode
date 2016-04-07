

class Solution(object):
    
    def dfs(self, nums, list, deal, i):
        if i == len(nums):
            return None
        deal.append(nums[i])
        list.append(deal[:])
        self.dfs(nums, list, deal, i+1)
        deal.pop()
        self.dfs(nums, list, deal, i+1)
        
    def subsets(self, nums):
        deal = []
        list = []
        list.append(deal)
        nums.sort()
        self.dfs(nums, list, deal, 0)
        return list
        
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """