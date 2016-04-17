# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#先序遍历，但要注意存好根节点和右节点
class Solution(object):
    
    #递归外保存根节点
    def __init__(self):
        self.reNode = None
    
    #中序遍历    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not hasattr(root, 'val'):
            return None
        reRight = root.right
        if self.reNode != None:
            self.reNode.left = None
            self.reNode.right = root
        self.reNode = root
        self.flatten(root.left)
        self.flatten(reRight)