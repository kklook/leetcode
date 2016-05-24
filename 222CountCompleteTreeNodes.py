class Solution(object):
    
    def countNodes(self, root):
        if root == None or not hasattr(root, 'val'):
            return 0
        lh, rh = 0, 0
        rl = root.left
        while rl != None:
            lh += 1
            rl = rl.left
        rr = root.right
        while rr != None:
            rh += 1
            rr = rr.right
        if rh == lh:
            return pow(2, rh + 1) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1  # 要加上自己