

#Ö±½ÓÄ£Äâ
class Solution(object):
    
    def deleteDuplicates(self, head):
        if not hasattr(head, 'val'):
            return head
        p = head
        front = ListNode(None)
        front.next = p
        result = front
        while p.next != None:
            if p.val == p.next.val:
                t = p.next
                while t.next != None and t.next.val == p.val:
                    t = t.next
                if t.next == None:
                    front.next = None
                    p = front
                else:
                    front.next = t.next
                    p = front.next
            else:
                front = front.next
                p = p.next
        return result.next