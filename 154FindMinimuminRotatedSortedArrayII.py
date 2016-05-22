# 二分, 当遇到mid 和 right 相等时, 将他俩分开处理
class Solution(object):
    
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid+1:]))
        return nums[left]