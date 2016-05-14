class Solution(object):
    
    def hasCycle(self, head):
        if not hasattr(head, 'val'):
            return False
        slow, fast = head, head
        while True:
            if slow.next == None:
                return False
            if fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True