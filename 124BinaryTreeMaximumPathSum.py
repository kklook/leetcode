

#dfs
class Solution(object):
    
    def maxPathSum(self, root):
        self.result = None
        def dfs(root):
            left, right = 0, 0
            val = root.val
            if root.left != None:
                left = dfs(root.left)
            if root.right != None:
                right = dfs(root.right)
            self.result = max(max(left, 0) + max(right, 0) + root.val, self.result)
            return max(left, right, 0) + root.val  
        if not hasattr(root, 'val'):
            return root
        else:
            dfs(root)
            return self.result