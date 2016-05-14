class Solution(object):
    
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        # 这个就是撞圈找环都能懂
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        # slow 走过d = 环起点 + slow走过圈数 * 环大小 + 距离环起点距离
        # 前面fast 走过 2d = 环起点 + fast走过圈数 * 环大小 + 距离环起点距离
        # d = (slow走过圈数 -  fast走过圈数) * 环大小 = 环起点 + slow走过圈数 * 环大小 + 距离环起点距离
        # 环起点 + 距离环起点距离 是 环大小的整数倍
        # 所以再下面, slow fast 相遇时一定是 slow 又走过了环起点到达了环开始节点 fast 也走过了环起点两节点相遇！
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow