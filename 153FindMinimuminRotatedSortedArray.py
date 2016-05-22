# 二分, 网上有个答案, 那个人显然不会写二分
class Solution(object):
    
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        result = nums[0]
        while left < right:
            mid = (right + left) / 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]