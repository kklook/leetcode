

#dfs 但要注意去除0的干扰
class Solution(object):
    
    def dfs(self, root):
        left, right = 0, 0
        if root.left != None:
            left = self.dfs(root.left)
        if root.right != None:
            right = self.dfs(root.right)
        if left != 0 and right != 0:
            return min(left, right) + 1
        elif left != 0:
            return left + 1
        elif right != 0:
            return right + 1
        else:
            return 1
        
    def minDepth(self, root):
        if not hasattr(root, 'val'):
            return 0
        return self.dfs(root)