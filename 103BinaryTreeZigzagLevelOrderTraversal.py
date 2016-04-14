# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    def bfs(self, root, result):
        L = []
        L.append(root)
        result.append([root.val, ])
        while len(L) != 0:
            temp = []
            while len(L) != 0:
                t = L.pop(0)
                if t.left != None:
                    temp.append(t.left)
                if t.right != None:
                    temp.append(t.right)
            L = temp[:]
            if len(L) != 0:
                t = []
                for i in L:
                    t.append(i.val)
                result.append(t)    
        
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not hasattr(root, 'val'):
            return []
        result = []
        self.bfs(root, result)
        for i in range(1, len(result), 2):
            result[i].reverse()
        return result