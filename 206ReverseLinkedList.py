# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    
    def reverseList(self, head):
        l = ListNode(None)
        l.next = head
        if not hasattr(head,'val'):
            return None
        if head.next == None:
            return head
        temp = l.next

        while(temp.next != None):
            p = temp.next
            temp.next = p.next
            p.next = l.next
            l.next = p
        return l.next
        
        """
        :type head: ListNode
        :rtype: ListNode
        """