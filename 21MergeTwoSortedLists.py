# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not hasattr(l1, 'val'):
            return l2
        if not hasattr(l2, 'val'):
            return l1
        head = ListNode(None)
        p = ListNode(None)
        p.next = head
        while l1 != None and l2 != None:
            p = p.next
            if l1.val < l2.val:
                p.val = l1.val
                l1 = l1.next
            else:
                p.val = l2.val
                l2 = l2.next
            p.next = ListNode(None)
        if l1 != None:
            p = p.next
            p.val = l1.val
            p.next = l1.next
        if l2 != None:
            p = p.next
            p.val = l2.val
            p.next = l2.next
        return head