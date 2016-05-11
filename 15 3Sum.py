# 去重！
class Solution(object):
    
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    if not [nums[i], nums[left], nums[right]] in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return result