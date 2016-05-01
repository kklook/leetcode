

# 险些蒙逼，还是直接dfs好
class Solution(object):
    
    def rob(self, root):
        
        def dfs(root):
            if root == None:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            return root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])
        return max(dfs(root))  # 需要存起来在外面判断！