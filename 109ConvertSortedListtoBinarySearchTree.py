class Solution(object):
    
    def sortedListToBST(self, head):
        
        def dfs(head):
            if head == None:
                return None
            temp = TreeNode(None)
            fast = head
            slow = head
            temp.next = slow
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                temp = temp.next
            # mid
            fast = slow.next
            if fast == None:
                return TreeNode(head.val)
            root = TreeNode(slow.val)
            if temp.next != head:
                temp.next = None
                root.left = dfs(head)
            else:
                root.left = None
            root.right = dfs(fast)
            return root
        
        return dfs(head)