class Solution(object):
    
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] < target - nums[i] - nums[j]:
                        left += 1
                    elif nums[left] + nums[right] > target - nums[i] - nums[j]:
                        right -= 1
                    else:
                        r = [nums[i], nums[j], nums[left], nums[right]]
                        if not r in result:
                            result.append(r)
                        left += 1
                        right -= 1
        return result