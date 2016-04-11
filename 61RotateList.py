# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not hasattr(head,'next'):
            return []
        list_listnode = []
        p = head
        j = 0
        while(p != None):
            j += 1
            list_listnode.append(p)
            p = p.next
        k = k%j
        if k == 0:
            return head
        list_listnode[-1].next = head
        list_listnode[-k-1].next = None
        return list_listnode[-k]