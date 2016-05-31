# left.left == right.right and left.right == right.left
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isSame(left, right):
            if left == None and right == None:
                return True
            elif (left == None and right != None) or (left != None and right == None):
                return False
            else:
                return left.val == right.val and isSame(left.left, right.right) and isSame(left.right, right.left)
                
        return isSame(root.left, root.right)