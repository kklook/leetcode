# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def solution(self,root,s,result):
        s.append(root.val)
        if root.left!=None:
            self.solution(root.left,s,result)
        if root.right!=None:
            self.solution(root.right,s,result)
        if root.left==None and root.right==None:
            temp=[]
            for i in s:
                temp.append(str(i))
            result.append("->".join(temp))
        s.pop()
    def binaryTreePaths(self, root):
        if not hasattr(root,'val'):
            return []
        s=[]
        result=[]
        self.solution(root,s,result)
        return result