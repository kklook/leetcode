

#Ö±½ÓÄ£Äâ
class Solution(object):
    
    def deleteDuplicates(self, head):
        if not hasattr(head, 'val'):
            return head
        p = head
        result = p
        while p.next != None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return result