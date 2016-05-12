# 抵制白板从我做起！
class Solution(object):
    
    def invertTree(self, root):

        def dfs(root):
            if root.left != None:
                dfs(root.left)
            if root.right != None:
                dfs(root.right)
            root.left, root.right = root.right, root.left
            
        if not hasattr(root, 'val'):
            return []
        dfs(root)
        return root