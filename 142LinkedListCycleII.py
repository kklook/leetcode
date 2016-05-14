# Floyd判圈
class Solution(object):
    def detectCycle(self, head):
        if not hasattr(head, 'val'):
            return None
        slow, fast = head, head
        while True:
            if slow.next == None or fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow