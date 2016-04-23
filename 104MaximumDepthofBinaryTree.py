

#dfs
class Solution(object):

    def dfs(self, root):
        if root == None:
            return 1
        left, right = 0, 0
        if root.left != None:
            left = self.dfs(root.left)
        if root.right != None:
            right = self.dfs(root.right)
        return max(left, right)+1
        
    def maxDepth(self, root):
        if not hasattr(root, 'val'):
            return 0
        return self.dfs(root)