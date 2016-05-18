# 写的漂亮吧
class Solution(object):
    
    def sortedArrayToBST(self, nums):
        
        def dfs(nums):
            if len(nums) == 0:
                return None
            root = TreeNode(None)
            mid = (len(nums) - 1) / 2
            root.val = nums[mid]
            root.left = dfs(nums[:mid])
            root.right = dfs(nums[mid+1:])
            return root
            
        return dfs(nums)