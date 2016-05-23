# 滑动窗口
class Solution(object):
    
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right, pathsum = 0, 0, 0
        result = size + 1
        while right < size:
            while right < size and pathsum < s:
                pathsum += nums[right]
                right += 1
            while left < right and pathsum >= s:
                result = min(result, right - left)
                pathsum -= nums[left]
                left += 1
        return [0, result][result <= size]