# dfs
class Solution(object):
    
    def isSameTree(self, p, q):
        
        def dfs(p, q):
            # q == None and q == None
            if p == q:
                return True
            elif not p or not q:  # p == None or q == None
                return False
            else:
                if p.val == q.val:
                    result = True
                    result = result and dfs(p.left, q.left)
                    result = result and dfs(p.right, q.right)
                    return result
                else:
                    return False
        
        return dfs(p, q)