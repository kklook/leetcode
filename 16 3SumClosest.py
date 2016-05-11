class Solution(object):
    
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = None
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if result == None:
                    result = nums[left] + nums[right] + nums[i]
                if nums[left] + nums[right] < target - nums[i]:
                    if abs(target - result) > abs(target - nums[left] - nums[right] - nums[i]):
                        result = nums[left] + nums[right] + nums[i]
                    left += 1
                elif nums[left] + nums[right] > target - nums[i]:
                    if abs(target - result) > abs(target - nums[left] - nums[right] - nums[i]):
                        result = nums[left] + nums[right] + nums[i]
                    right -= 1
                else:
                    return target
        return result
                    