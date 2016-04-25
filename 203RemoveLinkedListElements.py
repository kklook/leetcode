

class Solution(object):
    
    def removeElements(self, head, val):
        if not hasattr(head, 'val'):
            return head
        p = head
        front = ListNode(None)
        front.next = p
        result = front
        while p != None:
            if p.val == val:
                front.next = p.next
            else:
                front = front.next
            p = p.next
        return result.next