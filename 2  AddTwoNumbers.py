

#Ö±½ÓÄ£Äâ
class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        head = ListNode(None)
        p = head
        sum = 0
        while l1 != None or l2 != None or sum != 0:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            p.next = ListNode(sum % 10)
            p = p.next
            sum /= 10
        return head.next