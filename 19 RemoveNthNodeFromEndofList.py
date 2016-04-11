# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_listnode = []
        p = head
        while(p != None):
            list_listnode.append(p)
            p = p.next
        if len(list_listnode) == 1:
            return []
        elif len(list_listnode) == n:
            return head.next
        list_listnode[-n-1].next = list_listnode[-n-1].next.next
        return head