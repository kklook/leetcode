

#哈哈这个偷天换日太有意思了
class Solution(object):
    
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next