# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    def IOT(self, root, L):
        if root.left != None:
            self.IOT(root.left, L)
        L.append(root.val)
        if root.right != None:
            self.IOT(root.right, L)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not hasattr(root, 'val'):
            return True
        L = []
        self.IOT(root, L)
        for i in range(len(L)-1):
            if L[i] >= L[i+1]:
                return False
        return True
        