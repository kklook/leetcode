# 1从后向前找逆序元素
# 2从后到逆序元素向前找比他大的元素
# 3交换
# 4从逆序元素后排序
class Solution(object):
    
    def nextPermutation(self, nums):
        nflag = len(nums) - 1
        while nflag > 0:
            if nums[nflag] > nums[nflag-1]:
                for i in range(len(nums) - 1, nflag - 1, -1):
                    if nums[i] > nums[nflag-1]:
                        nums[i], nums[nflag-1] = nums[nflag-1], nums[i]
                        break
                nums[nflag:] = sorted(nums[nflag:])
                return None
            nflag -= 1
        nums.sort()