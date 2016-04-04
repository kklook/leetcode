# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countsum(self,root,t,sum_i,result):
        t.append(root.val)
        if root.left!=None:
            self.countsum(root.left,t,sum_i,result)
        if root.right!=None:
            self.countsum(root.right,t,sum_i,result)
        if root.right==None and root.left==None:
            if sum(t)==sum_i:
                result.append(t[:])
        t.pop()
    def pathSum(self, root, sum_i):
        if not hasattr(root,'val'):
            return []
        t=[]
        result=[]
        self.countsum(root,t,sum_i,result)
        return result
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
