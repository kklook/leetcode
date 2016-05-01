

# 坑爹不能用val来判断必须用对象判断
class Solution(object)
    
    def lowestCommonAncestor(self, root, p, q)
        def serch(root, p, q)
            left = None
            right = None
            if p == root or q == root
                return root
            if root.left != None
                left = serch(root.left, p, q)
            if root.right != None
                right = serch(root.right, p, q)
            if left != None and right != None
                return root
            else
                return max(left, right)
                
        return serch(root, p, q)