

#maxsum = ai + maxsum > 0 ? maxsum : 0
class Solution(object):
    
    #¾ÍÊÇÒ»ÅÀÆÂ
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxsum = -sys.maxint
        partsum = 0
        start ,end = 0, 0
        for i in range(len(nums)):
            if partsum > 0:
                partsum += nums[i]
            else:
                partsum = nums[i]
            if partsum > maxsum:
                maxsum = partsum
        return maxsum