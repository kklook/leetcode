

#dfs
class Solution(object):
    
    def __init__(self):
        self.flag = True
        
    def dfs(self, root):
        if root == None:
            return 1
        left, right = 0, 0
        if root.left != None:
            left = self.dfs(root.left)
        if root.right != None:
            right = self.dfs(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right) + 1
        
    def isBalanced(self, root):
        if not hasattr(root, 'val'):
            return True
        self.dfs(root)
        return self.flag