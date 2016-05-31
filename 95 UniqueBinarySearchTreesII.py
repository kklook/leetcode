# 这个dfs写的太美了！
class Solution(object):
    
    def generateTrees(self, n):

        def dfs(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            result = []
            for i in range(left, right + 1):  # 左右节点的范围是None ~ right
                llist = dfs(left, i - 1)
                rlist = dfs(i + 1, right)
                for l in llist:
                    for r in rlist:
                        root = TreeNode(i)  # 这里是升序, 所以不需要判断
                        root.left = l
                        root.right = r
                        result.append(root)
            return result
            
        if n == 0:
            return []
        return dfs(1, n)