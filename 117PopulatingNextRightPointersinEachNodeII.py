# 一样的代码, 上次就加过处理了
class Solution(object):
    def connect(self, root):
        queue = [root]
        nowright = root
        nextright = root
        while queue:
            node = queue.pop(0)
            if not node:
                continue
            if node:
                if node.left:
                    queue.append(node.left)
                    nextright = node.left
                if node.right:
                    queue.append(node.right)
                    nextright = node.right
            if nowright == node:
                node.next = None
                nowright = nextright
            else:
                node.next = queue[0]