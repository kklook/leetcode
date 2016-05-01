

#dfs
class Solution(object):
    
    def hasPathSum(self, root, sum):
        self.sum = sum
        self.hassum = False
        def dfs(root, val):
            val += root.val
            if root.left != None:
                dfs(root.left, val)
            if root.right != None:
                dfs(root.right, val)
            if root.left == None and root.right == None and val == self.sum:
                self.hassum = True
        if not hasattr(root, 'val'):
            return False
        dfs(root, 0)
        return self.hassum