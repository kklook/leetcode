

#dfs
class Solution(object):
    
    def sumNumbers(self, root):
        self.result = 0
        def dfs(root, rstr):
            rstr += str(root.val)
            if root.left != None:
                dfs(root.left, rstr)
            if root.right != None:
                dfs(root.right, rstr)
            if root.left == None and root.right == None:
                self.result += int(rstr)
        if not hasattr(root, 'val'):
            return 0
        dfs(root, "")
        return self.result