# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    
    def copyRandomList(self, head):
        p = head
        while p != None:
            copy = RandomListNode(p.label)
            copy.next = p.next
            copy.random = p.random
            p.next = copy
            p = p.next.next
        
        p = head
        while p != None:
            if p.random != None:
                p.next.random = p.random.next
            p = p.next.next
        
        result = RandomListNode(0)
        p = head
        result.next = head
        t = result
        while p != None:
            result.next = p.next
            result = result.next
            p.next = p.next.next
            p = p.next
        return t.next