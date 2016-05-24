class Solution(object):
    
    def preorderTraversal(self, root):
        stack = []
        result = []
        node = root
        while node or stack:
            if node is None:
                node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            node = node.left
        return result