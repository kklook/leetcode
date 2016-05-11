class Solution(object):
    
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        d = {}
        for i in range(len(nums)):
            d[i] = nums[i]
        d = sorted(d.iteritems(), key = lambda x: x[1])
        while left < right:
            if d[left][1] + d[right][1] < target:
                left += 1
            elif d[left][1] + d[right][1] > target:
                right -= 1
            else:
                return [d[left][0], d[right][0]]
        return None