

#先得建个结果表要不超时
class NumArray(object):
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums) == 0:
            return None
        self.resultList = []
        self.resultList.append(nums[0])
        for i in nums[1:]:
            self.resultList.append(i + self.resultList[-1])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.resultList[j]
        return self.resultList[j] - self.resultList[i - 1]
