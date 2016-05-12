# 226非递归
class Solution(object):
    
    def invertTree(self, root):
        nodeList = []
        nodeList.append(root)
        while len(nodeList):
            i = nodeList.pop(0)
            if hasattr(i, 'val'):
                nodeList.append(i.left)
                nodeList.append(i.right)
                i.left, i.right = i.right, i.left
        return root