

# ��Щ�ɱƣ�����ֱ��dfs��
class Solution(object):
    
    def rob(self, root):
        
        def dfs(root):
            if root == None:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            return root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1])
        return max(dfs(root))  # ��Ҫ�������������жϣ�