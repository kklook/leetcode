# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#ʹ�ÿ���ָ��ƽ�������ٶ�����鲢����
class Solution(object):
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not hasattr(head, 'val'):
            return []
        return self.breakList(head)
    
    #ƽ��
    def breakList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow = head, head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        fast, slow = slow, slow.next
        fast.next = None
        front = self.breakList(head)
        behind = self.breakList(slow)
        return self.sort2List(front, behind)
    
    #����    
    def sort2List(self, front, behind):
        p = ListNode(None)
        result = p
        while front != None or behind != None:
            fval = sys.maxint if front == None else front.val
            bval = sys.maxint if behind == None else behind.val
            if fval < bval:
                p.next = front
                front = front.next
            else:
                p.next = behind
                behind = behind.next
            p = p.next
        return result.next