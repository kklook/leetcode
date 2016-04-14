# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def ITS(self, root, L):
        if root.left != None:
            self.ITS(root.left, L)
        L.append(root.val)
        if root.right != None:
            self.ITS(root.right, L)
            
    def inorderTraversal(self, root):
        if not hasattr(root, 'val'):
            return []
            
        L = []
        self.ITS(root, L)
        return L
        
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """